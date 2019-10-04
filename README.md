# GKE to BigQuery Testing

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
NOTE: Can be called using curl or by going directly to the service URL
