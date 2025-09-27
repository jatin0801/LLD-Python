from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(Notification):

    def send(self, message: str):
       print("Send email noti:", message)

class SMSNotification(Notification):
    
    def send(self, message: str):
       print("Send sms noti:", message)


class PushNotification(Notification):
    def send(self, message: str):
       print("Send push noti:", message)

class NotificationFactory(ABC):
    @staticmethod
    @abstractmethod
    def notifier() -> Notification:
        pass

class EmailFactory(NotificationFactory):
    @staticmethod
    def notifier():
        return EmailNotification()

class SMSFactory(NotificationFactory):
    @staticmethod
    def notifier():
        return SMSNotification()

class PushFactory(NotificationFactory):
    @staticmethod
    def notifier():
        return PushNotification()

# class NotificationFactory:
#     def get_notification(self, notification_type: str) -> Notification:
#         if notification_type == "email":
#             return EmailNotification()
#         elif notification_type == "sms":
#             return SMSNotification()
#         elif notification_type == "push":
#             return PushNotification()
#         else:
#             raise ValueError("Unknown notification")



if __name__ == "__main__":
    # Abstract Factory Pattern
    # email_factory = EmailFactory()
    email_notifier = EmailFactory.notifier()
    email_notifier.send("Welcome to the system!")

    # factory = NotificationFactory()
    # email = factory.get_notification("email")
    # email.send("Welcome to the system!")

    # sms = factory.get_notification("sms")
    # sms.send("Your OTP is 123456")

    # push = factory.get_notification("push")
    # push.send("You have a new message")
