In order to run the webapp:
1) create a virtual environment using 'venv' or 'virtualenv'
2) install requirements from requirements.txt
3) run 'python3 manage.py runserver'

To use the solver, go to:
localhost:8000/{word}/{letters}

where {word} is the word you want to steal, and {letters} are the
letters available on the board. If {letters} is left blank, it will
show all words possible.




### John's notes
sudo apt-get install python3-pip

virtualenv env

pip3 install -r requirements.txt
pip3 install --upgrade django

python -m django --version # 2.0.2
python3 -m django --version # 2.0.2

pip3 install nltk

pip install --upgrade django



### Docker
 docker build -t jlanghauser/snatch-solver .
 docker run -p 8000:8000 jlanghauser/snatch-solver:latest
 docker container exec -it <CONTAINER_NAME> sh
 

