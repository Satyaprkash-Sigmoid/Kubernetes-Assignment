# kubernetes-assignment


Create deployment and service for above airflow and postgres (you can use postgres helm chart for postgres deployment)

Deploy airflow and postgres

Schedule the dag

Validate entry in postgres


Running fine - 
![Image](https://github.com/Satyaprkash-Sigmoid/Kubernetes-assignment/blob/master/Airflow_running_on_Kubernetes.png)
<<<<<<< HEAD


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
=======
>>>>>>> 10dff3c74b50b73f1286c332069685b58cedc6ba
