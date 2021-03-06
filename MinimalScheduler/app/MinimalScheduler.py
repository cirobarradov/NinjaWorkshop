from __future__ import print_function

import sys
import time
import socket
import signal
import getpass
from threading import Thread
import redis

from pymesos import MesosSchedulerDriver, Scheduler, encode_data
from addict import Dict

TERMINAL_STATES = ["TASK_FINISHED","TASK_FAILED","TASK_KILLED","TASK_ERROR","TASK_LOST"]
#DOCKER_TASK= 'cirobarradov/executor-app'
#TASK_CPU = 0.5
#TASK_MEM = 100

class MinimalScheduler(Scheduler):

    def __init__(self, redis_server, redis_key, docker_task, task_cpu, task_mem):
        self._id=0
        #init redis connection
        self._connection= redis.StrictRedis(host=redis_server)
        self._redis_key= redis_key
        # <redis_server> <redis_key> <task_id>
        self._command= '/app/task.sh {} {} '.format(redis_server, redis_key)
        self._docker_task=docker_task
        self._task_cpu=float(task_cpu)
        self._task_mem=float(task_mem)

    # Invoked when the scheduler successfully registers with a Mesos master.A unique ID (generated by the master) used for
    # distinguishing this framework from others and MasterInfo with the ip and port of the current master are provided
    # as arguments.
    def registered(self, driver, frameworkId, masterInfo):
        # set max tasks to framework registered
        logging.info("registered with frameworkId %s and Masterinfo: %s", frameworkId['value'],masterInfo)

    #Invoked when the scheduler re - registers with a newly elected Mesos master.This is only called when the scheduler
    #has previously been registered. MasterInfo containing the updated information about the elected master is provided
    #as an argument.
    def reregistered(self, driver, masterInfo):
        logging.info("re-registered with new master info: %s", masterInfo)

    #Invoked when resources have been offered to this framework.A single offer will only contain resources from a single
    #slave. Resources associated with an offer will not be re-offered to _this_framework until either this framework has
    #rejected those resources or those resources have been rescinded.
   def resourceOffers(self, driver, offers):
    filters = {'refuse_seconds': 5}

    for offer in offers:
        logging.info("offer: %s", offer)
        #logging.info("resources: %s", offer.resources)
        try:
            #get cpus and mem resources
            cpus = self.getResource(offer.resources, 'cpus')
            mem = self.getResource(offer.resources, 'mem')

            #evaluate if cpus and mem suit fit with task resources
            if cpus < self._task_cpu or mem < self._task_mem:
                continue

            #create task
            task = Dict()
            self._id += 1
            task_id = str(self._id)
            task.task_id.value = task_id
            task.agent_id.value = offer.agent_id.value
            task.name = 'task {}'.format(task_id)

            task.container.type = 'DOCKER'
            #task.container.docker.image = DOCKER_TASK #os.getenv('DOCKER_TASK')
            task.container.docker.image= self._docker_task
            task.container.docker.network = 'HOST'
            task.container.docker.force_pull_image = True

            task.command.shell = True
            #<redis_server> <redis_key> <task_id>
            task.command.value = self._command+task_id
            #resources
            task.resources = [
                dict(name='cpus', type='SCALAR', scalar={'value': self._task_cpu}),
                dict(name='mem', type='SCALAR', scalar={'value': self._task_mem}),
            ]
            logging.info("launching task " + task_id)
            #logging.info("task info =  %s", task)
            driver.launchTasks(offer.id, [task], filters)
        except Exception as e:
            logging.info(str(e))
            driver.declineOffer(offer.id, filters)
        pass

    #Invoked when the status of a task has changed(e.g., a slave is lost and so the task is lost, a task finishes and an
    #executor sends a status update saying so, etc).
    def statusUpdate(self, driver, update):
    #check update.state
    # logging.info(update)
    if (update.state in TERMINAL_STATES):
        if update.state == 'TASK_FAILED':
            logging.debug('######\n Status update: Failed %s \n ######', update.message)
        elif update.state == 'TASK_ERROR':
            logging.debug('######\n Status update: Error %s \n ######', update.message)
        elif update.state == 'TASK_FINISHED':
            try:
                logging.debug('######\n  Status update: Task %s FINISHED with this result %s \n ######',
                              update.task_id.value,
                              self._connection.hget(self._redis_key, update.task_id.value))
            except Exception as e:
                logging.error(str(e))
    else:
        logging.debug('######\n Status update: \n task_id: %s \n task_state: %s \n source: %s \n '
                      'agent_id %s \n executor_id %s \n container_status %s \n ######',
                      update.task_id.value,
                      update.state,
                      update.source,
                      update.agent_id,
                      update.executor_id,
                      update.container_status)


    # get resource from offer given the name of the resource
    def getResource(self, res, name):
        for r in res:
            if r.name == name:
                return r.scalar.value
        return 0.0

def main(master, redis_server, redis_key, docker_task, task_cpu, task_mem):

    #init framework with name, user and host
    framework = Dict()
    framework.user = getpass.getuser()
    framework.name = "MinimalFramework"
    framework.hostname = socket.gethostname()

    #init driver
    driver = MesosSchedulerDriver(
        MinimalScheduler(redis_server,redis_key, docker_task, task_cpu, task_mem),
        framework,
        master,
        use_addict=True,
    )

    def signal_handler(signal, frame):
        driver.stop()

    def run_driver_thread():
        driver.run()

    driver_thread = Thread(target=run_driver_thread, args=())
    driver_thread.start()

    print('Scheduler running, Ctrl+C to quit.')
    signal.signal(signal.SIGINT, signal_handler)

    while driver_thread.is_alive():
        time.sleep(1)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) <= 4:
        print("Usage: {} <mesos_master_ip> <redis_server> <redis_key> <docker_task> <task_cpu> <task_mem>".format(sys.argv[0]))
        sys.exit(1)
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
