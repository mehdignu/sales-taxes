from flask import Flask, render_template, request
from utils import format_request

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if (request.method == 'POST'):
        format_request(request.form)
    return render_template('index.html')



