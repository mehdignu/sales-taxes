from flask import Flask, render_template, request
from utils import format_request, calculate_goodies_prices, show_reciept

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if (request.method == 'POST'):
        goodies = format_request(request.form)
        basket = calculate_goodies_prices(goodies)
        show_reciept(goodies, basket)
    return render_template('index.html')



