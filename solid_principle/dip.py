
# A NotificationService directly creates and uses an EmailSender.
# Tomorrow you want to send via SMS or PushNotification.
# Task: Apply DIP so that NotificationService doesn’t depend on a specific message sender.


from abc import ABC, abstractmethod
class Notification(ABC):

    @abstractmethod
    def send(self): pass

class EmailSender(Notification):

    def send(self):
        print("send email")

class PushNotification(Notification):

    def send(self):
        print("send push notification")


class SMS(Notification):

    def send(self):
        print("sent SMS")


def send_notification(notification: Notification):
    notification().send()

send_notification(EmailSender)
send_notification(SMS)
send_notification(PushNotification)

#  build a Payment Processing System that supports multiple payment methods (Credit Card, PayPal, UPI).

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self):pass

class CreditCard(PaymentMethod):
    def pay(self):
        print("creditCard payment")

class Paypal(PaymentMethod):
    def pay(self):
        print("Paypal payment")
    
class UPI(PaymentMethod):
    def pay(self):
        print("UPI payment")

def payment(payment_method: PaymentMethod):
    payment_method().pay()

payment(Paypal)
payment(UPI)
payment(Paypal)



class Connection(ABC):

    @abstractmethod
    def connect(self, url):pass

class Mysql(Connection):
    def connect(self, url):
        print("connecting to mysql via url ", url)


def db_connect(connection: Connection, url):
    connection().connect(url)

db_connect(Mysql, "mysql://")
