class Burger():
    """
    汉堡
    """
    name=""
    price=0.0
    type='BURGER'
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class CheeseBurger(Burger):
    def __init__(self):
        self.name="cheese burger"
        self.price=10.0
class SpicyChickenBurger(Burger):
    def __init__(self):
        self.name="spicy chicken burger"
        self.price=15.0

class Snack():
    """
    小食类
    """
    name = ""
    price = 0.0
    type = "SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name
class Chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0
class ChickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0

class Beverage():
    """
    饮料
    """
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name
class Coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0
class Milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0
#以上的Burger，Snack，Beverage，都可以认为是该快餐店的产品，由于只提供了抽象方法，我们把它们叫抽象产品类，而cheese burger等6个由抽象产品类衍生出的子类，叫作具体产品类。

class FoodFactory():
    """
    抽象工厂foodFactory为抽象的工厂类，而burgerFactory，snackFactory，beverageFactory为具体的工厂类。
    """
    type=""
    def createFood(self,foodClass):
        print(self.type," factory produce a instance.")
        foodIns=foodClass()
        return foodIns
class BurgerFactory(FoodFactory):
    def __init__(self):
        self.type="BURGER"
class SnackFactory(FoodFactory):
    def __init__(self):
        self.type="SNACK"
class BeverageFactory(FoodFactory):
    def __init__(self):
        self.type="BEVERAGE"

if  __name__=="__main__":
    burger_factory=BurgerFactory()
    snack_factory=SnackFactory()
    beverage_factory=BeverageFactory()
    cheese_burger=burger_factory.createFood(CheeseBurger)
    print(cheese_burger.getName(),cheese_burger.getPrice())
    chicken_wings=snack_factory.createFood(ChickenWings)
    print(chicken_wings.getName(),chicken_wings.getPrice())
    coke_drink=beverage_factory.createFood(Coke)
    print(coke_drink.getName(),coke_drink.getPrice())