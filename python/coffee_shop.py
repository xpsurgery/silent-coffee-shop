# Instances of CoffeeFlavour will be the Flyweights
class CoffeeFlavour:

    def __init__(self, newFlavor):
        self.name = newFlavor

# Menu acts as a factory and cache for CoffeeFlavour flyweight objects
class Menu:

    def __init__(self):
        self.flavours = {}

    def lookup(self, flavourName):
        if flavourName not in self.flavours:
            self.flavours[flavourName] = CoffeeFlavour(flavourName)
        return self.flavours[flavourName]

class Order:

    def __init__(self, tableNumber, flavor):
        self.tableNumber = tableNumber
        self.flavour = flavor

    def serve(self):
        pass

class CoffeeShop:

    def __init__(self):
        self.orders = []
        self.menu = Menu()

    def takeOrder(self, flavourName, table):
        flavour = self.menu.lookup(flavourName)
        order = Order(table, flavour)
        self.orders.append(order)

    def service(self):
        for order in self.orders:
            order.serve()

