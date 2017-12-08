#Bicycle object
class Bicycle:
    def __init__(self, modelName, weight, cost):
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
#BikeShop object
class BikeShops:
    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = [Bicycle]
        self.margin = margin
        self.profit = 0
#Customer object
class Customers:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.canbuy = []
        self.own = []
#list of bike that BikeShop inventory
bikes = [Bicycle("Xe1", 4, 100),
         Bicycle("Xe2", 5, 200),
         Bicycle("Xe3", 6, 300),
         Bicycle("Xe4", 7, 400),
         Bicycle("Xe5", 8, 500),
         Bicycle("Xe6", 9, 600)]
#instance of BikeShops
bikeShops = BikeShops("ShopXeDap", bikes, 1.2)
#list instance of Customer
customers = [Customers("Phan", 200),
             Customers("Trung", 500),
             Customers("Viet", 1000)]
#Print name & cal what customers can buy
for c in customers:
    print(c.name)
    #Can buy
    for bike in bikes:
        number = int(c.fund / bike.cost)
        if number != 0:
            c.canbuy.append([bike.modelName, number])
#indicates what customers can buy
for c in customers:
    print(c.name + " can buy: ")
    print(c.canbuy)
#everyone purchase
for c in customers:
    print(c.name +" choose: ")
    for cb in c.canbuy:
        if cb[:][1] == 1:
            c.own = cb
            print(c.own)
            break
#cal profit of shop
for c in customers:
    for bike in bikes:
        if(c.own[:][0]) == bike.modelName:
            bikeShops.profit += bike.cost*bikeShops.margin

print(bikeShops.name + " have profit: " + str(bikeShops.profit))


