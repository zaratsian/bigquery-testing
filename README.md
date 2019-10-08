# GKE to BigQuery Testing

### Setup.sh

The ```setup.sh``` script will execute all of the commands needed to spin up a GKE cluster and deploy the resources and services. Alternatvely, the individual commands are listed below.

### Create GKE Cluster

```bash
gcloud container clusters create bqtimetest-app \
   --num-nodes 1 \
   --enable-basic-auth \
   --issue-client-certificate \
   --zone us-east1
```

### Check that nodes are up
```bash
kubectl get nodes
```

### Deploy resource to GKE cluster
```bash
kubectl apply -f deployment.yaml
```

### Check status of Deployment
```bash
kubectl get deployments
```

### Get pod status
```bash
kubectl get pods
```

### Create service
```bash
kubectl apply -f service.yaml
```

### Get service status
```bash
kubectl get services
```

### Access App

The ```kubectl get services``` commands will output an external IP address. Use this IP address to run your test query.

For example, if the IP is 35.34.231.211, then you can hit this url to get your results: http://35.34.231.211/query
