class Product:
    def __init__(self, description, price, quantity, dimension):
        self.description = description
        self.price = price
        self.quantity = quantity
        self.dimension = dimension

    def __str__(self):
        return f'{self.description}  \tUSD {self.price}  \t{self.quantity} unit(s)\t{self.dimension}'

class Buyer:
    def __init__(self, name, surname, mobile_phone):
        self.name = name
        self.surname = surname
        self.mobile_phone = mobile_phone

    def __str__(self):
        return f'{self.name} {self.surname} {self.mobile_phone}'

class Order:
    def __init__(self, title):
        self.title = title
        self.orders = []
        self.total_price = 0
        self.quantity = 1
        self.index = 0

    def add_order(self, product):
        if product not in self.orders:
            self.orders.append(product)
            self.total_price += product.price
        else:
            product.quantity += 1
            self.orders[self.orders.index(product)] = product
            self.total_price += product.price

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.orders):
            self.index += 1
            return self.orders[self.index - 1]
        raise StopIteration

    def __str__(self):
        return f"{self.title}\n{'-' * 30}\n" + '\n'.join(map(str, self.orders)) + '\n' +\
                'Total: USD ' + f'{self.total_price:.2f}' + '\n'

product_1 = Product('onion', 1.00, 1, 'sack package')
product_2 = Product('lemon', 2.00, 1, 'pieces')
product_3 = Product('Banana', 3.00, 1, 'brush')

# print (product_3)
# print ()

buyer_1 = Buyer('Barak', 'Obama', '+38-066-221-34-54')
buyer_2 = Buyer('Leondardo', 'dicaprio', '+38-063-344-99-87')
buyer_3 = Buyer('Vasiliy', 'Vasilev', '+38-098-223-65-09')

buyer_1_order = Order('Buyer_1_Order')
buyer_1_order.add_order(product_1)
buyer_1_order.add_order(product_2)
# print (buyer_1_order)

buyer_2_order = Order('Buyer_2_Order')
buyer_2_order.add_order(product_2)
buyer_2_order.add_order(product_2)
buyer_2_order.add_order(product_3)
# print (buyer_2_order)

buyer_3_order = Order('Buyer_3_Order')
buyer_3_order.add_order(product_1)
buyer_3_order.add_order(product_2)
buyer_3_order.add_order(product_3)
buyer_3_order.add_order(product_3)
# print (buyer_3_order)
# print()
print (buyer_3_order.__next__())
print (buyer_3_order.__next__())
print (buyer_3_order.__next__())
print ()
for products in buyer_3_order:
    print(products)
