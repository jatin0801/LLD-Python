from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass

    @abstractmethod
    def refund(self, amount: float):
        print("Refunding via generic method:", amount)
        # pass

class UPIPayment(Payment):

    def pay(self, amount: float):
       print("Paying via UPI:", amount)

    def refund(self, amount: float):
        # pass
       print("Refunding via UPI:", amount)

if __name__ == "__main__":
    upi = UPIPayment()
    upi.pay(1000)
    upi.refund(599)