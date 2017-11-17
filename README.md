# Mesos Workshop

[![N|Solid](http://www.datio.com/wp-content/uploads/2016/09/logo-1.png)](http://www.datio.com/)

## Sumary
This is a workshop for ninja academy with an example of the mesos api implementation. 

## Content

  - [Docker container with an example of a minimal scheduler implementation with python](https://github.com/cirobarradov/NinjaWorkshop/tree/master/MinimalScheduler)
  - [Basic Marathon examples](https://github.com/cirobarradov/NinjaWorkshop/tree/master/marathon)

## Steps
  - Install [Docker](https://docs.docker.com/engine/installation/)
  - Install and run [minimesos](http://minimesos.readthedocs.io/en/latest/) tool
  
  [![N|Solid](https://pbs.twimg.com/profile_images/651035760968110080/WMuud6Bi.png)](http://minimesos.readthedocs.io/en/latest/)
  
```sh
$ curl -sSL https://minimesos.org/install | sh
$ export PATH=$PATH:$HOME/.minimesos/bin
$ minimesos init
$ minimesos up
  Minimesos cluster is running: 1145206142
  Mesos version: 1.0.0
  export MINIMESOS_NETWORK_GATEWAY=172.17.0.1
  export MINIMESOS_AGENT=http://172.17.0.7:5051; export MINIMESOS_AGENT_IP=172.17.0.7
  export MINIMESOS_ZOOKEEPER=zk://172.17.0.3:2181/mesos; export MINIMESOS_ZOOKEEPER_IP=172.17.0.3
  export MINIMESOS_MARATHON=http://172.17.0.6:8080; export MINIMESOS_MARATHON_IP=172.17.0.6
  export MINIMESOS_CONSUL=http://172.17.0.8:8500; export MINIMESOS_CONSUL_IP=172.17.0.8
  export MINIMESOS_MESOSDNS=http://172.17.0.4:53; export MINIMESOS_MESOSDNS_IP=172.17.0.4
  export MINIMESOS_MASTER=http://172.17.0.5:5050; export MINIMESOS_MASTER_IP=172.17.0.5

```  
  - Implement mesos scheduler sample with pymesos and install it into a docker container
  - Create an automated build [Docker Registry](https://hub.docker.com/) with the sample scheduler containerized
  - Deploy on [marathon](https://github.com/cirobarradov/NinjaWorkshop/tree/master/marathon)
