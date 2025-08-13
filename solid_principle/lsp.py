#  building a transportation system with different types of vehicles 

from abc import ABC, abstractmethod

class Vehicles(ABC):
    pass

class FueldVehicle(Vehicles):

    @abstractmethod
    def refuel(self):
        pass

class ElectricVehicle(Vehicles):
    @abstractmethod
    def charging(self):
        pass

class HumanPower(Vehicles):
    @abstractmethod
    def pedal(self):
        pass



class Car(FueldVehicle):
    
    def refuel(self):
        print("refueling the car")

class ElectricCar(ElectricVehicle):

    
    def charging(self):
        print("Charging the electric car")

class Bicyle(HumanPower):
    def pedal(self):
        print ("use pedal for bicyle")
    


ElectricCar().charging()
Bicyle().pedal()
Car().refuel()


# Bird and Ostrich problem

class Bird(ABC):
    @abstractmethod
    def makesound(self):
        pass

class FlyingBird(Bird):

    @abstractmethod
    def fly(self):
        pass

class NonFlyingBird(Bird):
    def walk(self):
        pass


class Sparrow(FlyingBird):
    def makesound(self):
        print("making sound")

    def fly(self):
        print("can fly")

class Orchid(NonFlyingBird):
    def makesound(self):
        print("making sound")

    def walk(self):
        print("can't fly , run")

Orchid().walk()
Orchid().makesound()
Sparrow().fly()
Sparrow().makesound()

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    pass

class CashlessPayment(PaymentMethod):
    
    @abstractmethod
    def pay(self):
        pass
class CashPayment(PaymentMethod):

    @abstractmethod
    def cash_pay(self):
        pass
    


class CreditCard(CashlessPayment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class PayPal(CashlessPayment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


class CashOnDelivery(CashPayment):
    def cash_pay(self, amount):
        print("Cash on Delivery payment ")


def complete_purchase_cashless(payment: PaymentMethod, amount):
    payment.pay(amount)

def complete_purchase_on_cod(payment: PaymentMethod, amount):
    payment.cash_pay(amount)

# Works fine
complete_purchase_cashless(CreditCard(), 100)
complete_purchase_cashless(PayPal(), 200)
complete_purchase_on_cod(CashOnDelivery(), 300)

