In order to run the webapp:
1) create a virtual environment using 'venv' or 'virtualenv'
2) install requirements from requirements.txt
3) run 'python3 manage.py runserver'

To use the solver, go to:
localhost:8000/{word}/{letters}

where {word} is the word you want to steal, and {letters} are the
letters available on the board. If {letters} is left blank, it will
show all words possible.




## John's notes
sudo apt-get install python3-pip

virtualenv env

pip3 install -r requirements.txt
pip3 install --upgrade django

python -m django --version # 2.0.2
python3 -m django --version # 2.0.2

pip3 install nltk

pip install --upgrade django


### Docker
 docker build -t gcr.io/langatan/snatch-solver:latest .
 docker run -p 8000:8000 gcr.io/langatan/snatch-solver:latest 
 docker container exec -it <CONTAINER_NAME> sh
 
### Deployment 

#### You'll need access to the production langatan project/cluster
gcloud auth login
gcloud config set project langatan
docker push gcr.io/langatan/snatch-solver:latest
Will need to change the image name in k8 yaml
kubectl config get-contexts
kubectl config use-context gke_langatan_us-east1-b_main-cluster
kubectl apply -f k8s-pod.yaml 

#### This also has an ingress, we just aren't using it right now
kubectl apply -f ingress.yaml