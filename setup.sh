gcp_project_id="$(gcloud config get-value project)"

gcloud builds submit --tag gcr.io/"$gcp_project_id"/gke-bq-testing ./main/.

gcloud container clusters create bqtimetest-app \
   --num-nodes 1 \
   --enable-basic-auth \
   --issue-client-certificate \
   --zone us-east1

sed -i 's/gcp_project_id/'"$gcp_project_id"'/' deployment.yaml

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

echo ""
echo ""
echo ""
kubectl get services

#ZEND
