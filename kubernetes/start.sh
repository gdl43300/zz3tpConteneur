#!/bin/bash

# db
kubectl apply -f persistentVolume.yaml
kubectl apply -f dbConfigMap.yaml
kubectl apply -f dbServices.yaml
kubectl apply -f dbStatefulSet.yaml

# flask
kubectl apply -f flaskDeployment.yaml
kubectl apply -f flaskService.yaml
