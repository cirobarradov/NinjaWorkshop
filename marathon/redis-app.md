{
  "id": "redis",
  "cmd": null,
  "cpus": 1,
  "mem": 128,
  "disk": 0,
  "instances": 1,
  "container": {
    "docker": {
      "image": "redis",
      "network": "HOST",
      "forcePullImage": true
    },
    "type": "DOCKER"
  }
}
