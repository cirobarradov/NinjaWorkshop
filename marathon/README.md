# Running apps and frameworks with Marathon

minimesos

http://minimesos.readthedocs.io/en/latest/

marathon api 

https://dcos.io/docs/1.9/deploying-services/marathon-api

CREATE
```sh
$ export MINIMESOS_MARATHON_IP=172.17.0.x
$ vi pythonserver.json
$ curl -X POST http://$MINIMESOS_MARATHON_IP:8080/v2/apps -d @pythonserver.json -H  "Content-type: application/json"
```

GET

DESTROY
