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
```sh
$ curl -sSL https://minimesos.org/install | sh
$ export PATH=$PATH:$HOME/.minimesos/bin
$ minimesos init
$ minimesos up
```  
  - Implement mesos scheduler sample with pymesos and install it into a docker container
  - Create an automated build Docker Registry with the sample scheduler containerized
  - Deploy on marathon
