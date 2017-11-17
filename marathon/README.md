# Running apps and frameworks with Marathon

minimesos

http://minimesos.readthedocs.io/en/latest/

marathon api 

https://dcos.io/docs/1.9/deploying-services/marathon-api

### Create Tasks
Create and start a new application. Note: This operation will create a deployment. The operation finishes, if the deployment succeeds. You can query the deployments endoint to see the status of the deployment.

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
### Create Groups
Create and start a new application group. Application groups can contain other application groups.

  - Minimal Scheduler + Redis Server
```sh
$ vi ninja-scheduler-group.json
$ curl -X POST http://$MINIMESOS_MARATHON_IP:8080/v2/groups -d @ninja-scheduler-group.json -H  "Content-type: application/json"
```   

### Get
Get the application with id app_id. The response includes some status information besides the current configuration of the app. You can specify optional embed arguments, to get more embedded information.

```sh
$ curl -X GET http://$MINIMESOS_MARATHON_IP:8080/v2/apps -d @pythonserver.json -H  "Content-type: application/json"
```   
### Destroy
Destroy an application. All data about that application will be deleted. Note: This operation will create a deployment. The operation finishes, if the deployment succeeds. You can query the deployments endoint to see the status of the deployment.

```sh
$ curl -X GET http://$MINIMESOS_MARATHON_IP:8080/v2/apps -d @pythonserver.json -H  "Content-type: application/json"
```   
