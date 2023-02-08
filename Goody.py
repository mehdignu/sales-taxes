class Goody:
    def __init__(self, name, quantity, status, category, price):
        self.name = name
        self.quantity = quantity
        self.status = status
        self.category = category
        self.price = price
        self.tax = 0 

    def calculate_tax_rate(self):
        pass