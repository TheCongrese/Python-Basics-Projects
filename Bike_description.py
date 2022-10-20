# Object Oriented Programming.
class bike_d:
    def __init__(self, description, cost, sale_price, condition):
        self.description=description
        self.cost=cost
        self.sale_price=sale_price
        self.condition=condition
        self.sold = False

    def update_sale_price(self, sale_price):
        if self.sold == True:
            print('Action not allowed, Bike has already been sold')
        else:
            self.sale_price = self.sale_price

    def sell(self):
        self.sold= True

# Procedure Oriented Programming
# def update_sale_price(bike, sale_price):
#     if bike['sold'] == True:
#         print('Action not allowed, Bike has already been sold')
#     else:
#         bike['sale_price'] = sale_price
#
#
# def sell(bike):
#     bike['sold'] = True
#
#
# def create_bike(description, cost, sale_price, condition):
#     return {
#         'description': description,
#         'cost': cost,
#         'sale_price': sale_price,
#         'condition': condition,
#         'sold': False
#     }


bike1 = bike_d('Univega Alpina, orange', 100, 500, 0.5)
bike1.update_sale_price( 350)
bike1.sell()
bike1.update_sale_price( 350)

