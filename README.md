# spark-k8s-docker
The docker image for deploying spark app on kubernetes cluster

#### spark-3.1.1
#### java11
#### python3.7


## USAGE
The process is very simple, the spark application that needs to be deployed on spark k8s cluster should be added to <b>/opt/work-dir</b> like [this](https://github.com/arezamoosavi/spark-k8s-docker/blob/main/example/Dockerfile) or any other directory and build the docker image then push it to registery or whatever.