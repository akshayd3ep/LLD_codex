# Create a User class that stores data, sends email, and saves to database. Then split responsibilities.

class User:
    def __init__(self, name, email):
        self.username = name
        self.email = email

class MailSender:
    def send(self, userdata):
        print(f"sent email to {userdata.username} on email {userdata.username}")

class UserRecords:
    def save(self, userdata):
        print(f"stored on db>>  name: {userdata.username} email: {userdata.email}")
        

user = User("akshay", "00@gmail.com")
MailSender().send(user)
UserRecords().save(user)


# Order processing

class Order:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    
class CalculatePrice:
    def calculate(self, order):
        return order.price

class Tax:
    def tax_calculate(self, calculated_price, tax_rate):
        self.total = calculated_price +tax_rate
        print(f"total calculated price including tax is {self.total } ")

class OrderRecords:
    def save(self, order, gross_price, net_price ):
        print(f"stored on db: product_name:{order.name} gross price: {gross_price} taxed_price: {net_price.total}")


class EmailSender:
    def send(self, order , net_price):
        print(f"order confirmed {order.name} price {net_price.total}")

order1 = Order("shoes", 400)
calculate_price = CalculatePrice().calculate(order1)
tax_obj = Tax()
taxed_price = tax_obj.tax_calculate(calculate_price, 18)
OrderRecords().save(order1, calculate_price, tax_obj)
EmailSender().send(order1, tax_obj)


# Customer Registration System

class Customer:
    def __init__(self, name, email, phone):
        self.name = name 
        self.email = email
        self.phone = phone

class Validation:
    def validate(self, ip):
        if isinstance(ip, int) and len(str(ip)) == 12:
            return ip
        
        elif isinstance(ip, str) and "@" in ip:
            return ip

        else:
            False

class PhoneFormatter:
    def formatter(self, validate, phone):
        if validate:
            return f"+{str(phone)[:2]}-{2:}"

class CustomerRecord:
    def save(self, customer, validate):
        if validate:
            print(f"stored in db {customer.name} {customer.email} {customer.phone}")


class Email:
    def semt(self, customer, validate):
        if validate:
            print(f"email sent to  {customer.email} ")

cus1 = Customer("asr", "ao@gmail.com", 916203707621)
emailvalidate = Validation().validate(cus1.email)
phonevalidate = Validation().validate(cus1.phone)
phone_formats = PhoneFormatter().formatter(phonevalidate, cus1.phone)
CustomerRecord().save(cus1, phonevalidate)
Email().semt(cus1, phonevalidate)
