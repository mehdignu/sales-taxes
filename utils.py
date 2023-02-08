from itertools import islice
from Goody import Goody

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