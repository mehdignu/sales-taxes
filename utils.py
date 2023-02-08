from itertools import islice
from Goody import Goody
from Basket import Basket

def chunks(data, SIZE=10000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k:data[k] for k in islice(it, SIZE)}

def format_request(request):
    data_chunks = chunks(request, 5)
    goodies_list = []
    for data in data_chunks:
        keys = data.keys()
        name, quantity, status, category, price = [data[key] for key in keys]
        goody = Goody(name, quantity, status, category, price)
        goodies_list.append(goody)
    return goodies_list

def calculate_goodies_prices(goodies):
    total = 0
    for goody in goodies:
        goody.calculate_tax_rate()
        goody.calculate_price_with_tax()
        total = total+ goody.price_with_tax
    return Basket(total)

def show_reciept(goodies, basket):
    for goody in goodies:
        goody.display_goody()
    print(f'total is {basket.total}')