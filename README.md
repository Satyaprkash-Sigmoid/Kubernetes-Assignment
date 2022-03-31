# kubernetes-assignment
-> start docker
-> minikube start 
-> minikube dashboard
-> chmod +x ./script-create.sh 
-> ./script-create.sh
-> minikube mount ./dags/:/mnt/airflow/dags
-> kubectl exec -it puckel-deploy-698fd5d574-tff7g -- bash 
FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
export FERNET_KEY=$FERNET_KEY
airflow initdb
-> kubectl port-forward svc/puckel-service 8080:8080 