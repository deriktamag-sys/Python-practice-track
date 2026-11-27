###createw a class called Order which stores the item and price . use dunder function __gt__()to convey that :
#order1 > order2 if the price of the order 1 > order2 ..


class Order:

    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self, price):
        return self.price > odr2.price


odr1 = Order("chips", 50)
odr2 = Order("momo",120)

print(odr1<odr2)
        
        