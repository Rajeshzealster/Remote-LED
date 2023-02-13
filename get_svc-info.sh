#!/bin/bash

# Get the cluster IP and port of the webscoket-server-service service
service_cluster_ip=$(minikube kubectl -- get svc websocket-server-service -o jsonpath='{.spec.NodePort}')
service_port=$(minikube kubectl -- get svc websocket-server-service -o jsonpath='{.spec.ports[0].port}')

# Print the cluster IP and port
echo "Service Cluster IP: $service_cluster_ip"
echo "Service Port: $service_port"

