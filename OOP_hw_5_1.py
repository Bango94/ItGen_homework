import OOP_hw_5_1_module_order
import OOP_hw_5_1_module_product
import OOP_hw_5_1_module_buyer

product_1 = OOP_hw_5_1_module_product.Product('onion', 1.00, 'sack package')
product_2 = OOP_hw_5_1_module_product.Product('lemon', 2.00, 'pieces')
product_3 = OOP_hw_5_1_module_product.Product('Banana', 3.00, 'brush')

buyer_1 = OOP_hw_5_1_module_buyer.Buyer('Barak', 'Obama', '+38-066-221-34-54')
byuer_2 = OOP_hw_5_1_module_buyer.Buyer('Leondardo', 'dicaprio', '+38-063-344-99-87')
buyer_3 = OOP_hw_5_1_module_buyer.Buyer('Vasiliy', 'Vasilev', '+38-098-223-65-09')

buyer_1_order = OOP_hw_5_1_module_order.Order('Buyer_1_Order')
buyer_1_order.add_order(product_1)
buyer_1_order.add_order(product_2)
print (buyer_1_order)

buyer_2_order = OOP_hw_5_1_module_order.Order('Buyer_2_Order')
buyer_2_order.add_order(product_2)
buyer_2_order.add_order(product_3)
print (buyer_2_order)

buyer_3_order = OOP_hw_5_1_module_order.Order('Buyer_3_Order')
buyer_3_order.add_order(product_1)
buyer_3_order.add_order(product_2)
buyer_3_order.add_order(product_3)
print (buyer_3_order)
