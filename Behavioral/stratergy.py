from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: int):
        pass

class Cash(PaymentMethod):
    def pay(self, amount):
        print("Paying cash...", amount)

class UPI(PaymentMethod):
    def pay(self, amount):
        print("Paying UPI...", amount)

class Card(PaymentMethod):
    def pay(self, amount):
        print("Paying card...", amount)

class PaymentProcessor:
    def __init__(self, paymentMethod: PaymentMethod):
        self.payment_method = paymentMethod
    
    def process_payment(self, amount):
        print("Processing payment")
        self.payment_method.pay(amount)
    
    def set_payment(self, paymentMethod):
        self.payment_method = paymentMethod

if __name__ == "__main__":
    payment_processor = PaymentProcessor(Cash())
    payment_processor.process_payment(200)

    payment_processor.set_payment(UPI())
    payment_processor.process_payment(400)

    payment_processor.set_payment(Card())
    payment_processor.process_payment(600)