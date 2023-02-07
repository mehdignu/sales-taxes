
* configure virtual environment
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

* run the app in dev mode
export FLASK_APP=tax
export FLASK_ENV=development
flask run