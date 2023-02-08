
## configure virtual environment
```python
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```


## run the app in dev mode
```python
export FLASK_APP=tax
export FLASK_ENV=development
flask run
open http://127.0.0.1:5000
```
## assumptions
- categories and status (imported / other) is hardcoded, can be seperated into a enumerations but will add complexity on the frontend when adding dynamic tabs.
