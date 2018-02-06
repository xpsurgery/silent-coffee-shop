# Instances of CoffeeFlavour will be the Flyweights
class CoffeeFlavour:

    def __init__(newFlavor):
		self.name = newFlavor

# Menu acts as a factory and cache for CoffeeFlavour flyweight objects
class Menu:

    def __init__(self):
        flavours = {}

    def lookup(self, flavorName):
		if not flavours.containsKey(flavorName):
			flavours.put(flavorName, CoffeeFlavour(flavorName))
		return flavours.get(flavorName)

    def totalCoffeeFlavoursMade(self):
		return flavours.size()

class Order:

    def __init__(self, tableNumber, flavor):
		self.tableNumber = tableNumber
		self.flavour = flavor

    def serve(self):
        pass

class CoffeeShop:

    def __init__(self):
        orders = []
        menu = Menu()

    def takeOrder(self, flavourName, table):
		flavour = menu.lookup(flavourName)
		order = Order(table, flavour)
		orders.add(order)

    def service(self):
        for order in orders:
			order.serve()

