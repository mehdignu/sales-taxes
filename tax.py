from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        for key, val in request.form.items():
            print(key,val)
    return render_template('index.html')
