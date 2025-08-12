# ocp voilation
"""
class AreaCalculator:
    def calculate_area(self, shape):
        if shape["type"] == "circle":
            return 3.14 * shape["radius"] ** 2
        elif shape["type"] == "rectangle":
            return shape["width"] * shape["height"]
        else:
            return None


shapes = [
    {"type": "circle", "radius": 5},
    {"type": "rectangle", "width": 4, "height": 6}
]

calculator = AreaCalculator()
for s in shapes:
    print(calculator.calculate_area(s))


"""

from abc import ABC, abstractmethod

class Calculator(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Calculator):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Calculator):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        
shapes = [
    Circle(5),
    Rectangle(4, 5)
]

for shape in shapes:
    shape.area()

# designing a Payment Processing System.

from abc import ABC

class PaymentProcessing(ABC):

    def payment():
        pass

class CreditCard(PaymentProcessing):
    def __init__(self, cvv, expire, pin, cardno):
        self.cvv = cvv
        self.expire = expire
        self.pin = pin 
        self.cardno = cardno
    
    def payment(self):
        if self.cvv and self.expire and self.pin and self.cardno:
            print("card payment sucessfully")
            return " card payment done"

class Paypal(PaymentProcessing):
    def __init__(self, pin, paypalid):
        self.pin = pin 
        self.paypalid = paypalid
    
    def payment(self):
        if self.paypalid and self.pin:
            print("paypal payment sucessfully")
            return " paypal  payment done"

class UPI(PaymentProcessing):
    def __init__(self, pin, upiId):
        self.pin = pin 
        self.upiId = upiId
    
    def payment(self):
        if self.pin and self.upiId:
            print("UPI payment sucessfully")
            return " upi  payment done"

class Crypto(PaymentProcessing):
    def __init__(self, pin, crypID):
        self.pin = pin 
        self.crypID = crypID
    
    def payment(self):
        if self.pin and self.crypID:
            print("Crypto payment sucessfully")
            return " Crypto  payment done"


payments = [CreditCard(2345, "07/20", 2343, 987439874937497297294),
            Paypal(2345, 987439874937497297294),
            UPI(4342, 8209382093802984),
            Crypto(8098, 8302938209830)]

for payment in payments:
    payment.payment()