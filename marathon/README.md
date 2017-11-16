# Running apps and frameworks with Marathon

minimesos

http://minimesos.readthedocs.io/en/latest/

marathon api 

https://dcos.io/docs/1.9/deploying-services/marathon-api

### Create Methods

  - A simple task with marathon: built-in web server (SimpleHTTPServer)
```sh
$ export MINIMESOS_MARATHON_IP=172.17.0.x
$ vi pythonserver.json
$ curl -X POST http://$MINIMESOS_MARATHON_IP:8080/v2/apps -d @pythonserver.json -H  "Content-type: application/json"
```
  - Redis Server
```sh
$ vi pythonserver.json
$ curl -X POST http://$MINIMESOS_MARATHON_IP:8080/v2/apps -d @redis-app.json -H  "Content-type: application/json"
```  

  - Minimal Scheduler 
```sh
$ vi minimal-scheduler.json
$ curl -X POST http://$MINIMESOS_MARATHON_IP:8080/v2/apps -d @minimal-scheduler.json -H  "Content-type: application/json"
```  

  - Groups (Minimal Scheduler + Redis Server)
```sh
$ vi ninja-scheduler-group.json
$ curl -X POST http://$MINIMESOS_MARATHON_IP:8080/v2/groups -d @ninja-scheduler-group.json -H  "Content-type: application/json"
```   

GET

DESTROY
