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
            percent = lambda part, whole:float(whole) / 100 * float(part)
            calculated_price_with_tax = percent(self.tax, self.price) + self.price
            self.price_with_tax = round(calculated_price_with_tax, 2)
        else:
            self.price_with_tax = self.price

    def display_goody(self):
        print(self.quantity, self.status, self.name, self.price_with_tax)