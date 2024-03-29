
class Product:
    def __init__(self, description, price, dimensions):
        self.description = description
        self.price = price
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.description} {self.price} {self.dimensions}'

product_1 = Product('onion', '1.00', 'sack package')
product_2 = Product('lemon', '2.00', 'pieces')
product_3 = Product('Banana', '3.00', 'brush')


class Buyer:
    def __init__(self, name, surname, mobile_phone):
        self.name = name
        self.surname = surname
        self.mobile_phone = mobile_phone

    def __str__(self):
        return f'{self.name} {self.surname} {self.mobile_phone}'

buyer_1 = Buyer('Barak', 'Obama', '+38-066-221-34-54')
byuer_2 = Buyer('Leondardo', 'dicaprio', '+38-063-344-99-87')
buyer_3 = Buyer('Vasiliy', 'Vasilev', '+38-098-223-65-09')


class Order:
    def __init__(self, title):
        self.title = title
        self.orders = []
        self.total_price = []

    def add_order(self, product):
        if product not in self.orders:
            self.orders.append(product)
            self.total_price.append(product.price)

    def __str__(self):
        return f"{self.title}\n{'-' * 30}\n" + '\n'.join(map(str, self.orders)) + '\n' +\
                'Total: USD ' + f'{sum(map(float, self.total_price)):.2f}' + '\n'

buyer_1_order = Order('Buyer_1_Order')
buyer_1_order.add_order(product_1)
buyer_1_order.add_order(product_2)
print (buyer_1_order)

buyer_2_order = Order('Buyer_2_Order')
buyer_2_order.add_order(product_2)
buyer_2_order.add_order(product_3)
print (buyer_2_order)

buyer_3_order = Order('Buyer_3_Order')
buyer_3_order.add_order(product_1)
buyer_3_order.add_order(product_2)
buyer_3_order.add_order(product_3)
print (buyer_3_order)