class Customers:
    def __init__(self, name, beverage, food):
        self.name = name
        self.beverage = beverage
        self.food = food

    greeting = "Welcome to the Coffee Palace!"
    cinnamon_Price = 100
    glazedDoughnut_Price = 100
    icedCaffeLatte_Price = 125
    caramelMacchiato_Price = 130


# creating a instance for Samirah
c1 = Customers("Samirah", "Iced Caffe Latte", "Cinnamon Roll")

print(Customers.greeting + ", " + c1.name + "!")
print("Do you want your usual " + c1.beverage + "?")
print("For you, " + c1.name + ", Your total is: " + str(Customers.cinnamon_Price))

# creating an instance for Jerry
c2 = Customers("Jerry", "Caramel Macchiato", "Glazed Doughnut")
print("\nAnd you, " + c2.name + ". Do you want a " + c2.food + "with your " + c2.food)

print("And " + c2.name + ", Your total is: " + str(Customers.caramelMacchiato_Price + Customers.glazedDoughnut_Price) )
