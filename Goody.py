class Goody:
    def __init__(self, name, quantity, status, category, price):
        self.name = name
        self.quantity = quantity
        self.status = status
        self.category = category
        self.price = price
        self.tax = 10
        self.price_with_tax = 0

    def calculate_tax_rate(self):
        if self.category in ["books", "food", "medical"]:
            self.tax = 0
        if self.status == "imported":
            self.tax = self.tax + 5

    def calculate_price_with_tax(self):
        if self.tax != 0:
            calculated_price_with_tax = (self.price / self.tax) + self.price
            self.price_with_tax = round(calculated_price_with_tax, 2)
        else:
            self.price_with_tax = self.price