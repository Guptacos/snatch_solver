In order to run the webapp:
1) create a virtual environment using 'venv' or 'virtualenv'
2) install requirements from requirements.txt
3) run 'python3 manage.py runserver'

To use the solver, go to:
localhost:8000/{word}/{letters}

where {word} is the word you want to steal, and {letters} are the
letters available on the board. If {letters} is left blank, it will
show all words possible.

