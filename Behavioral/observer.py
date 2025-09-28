from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update():
        pass

class YoutubeSubscriber(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, video: str):
        print(f"Notify {self.name} about video {video}")

class EmailSubscriber(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, video: str):
        print(f"Email {self.name} about video {video}")

class PushSubscriber(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, video: str):
        print(f"Push {self.name} about video {video}")
        

class SocialChannel(ABC):
    @abstractmethod
    def addSubscriber():
        pass

    @abstractmethod
    def removeSubscriber():
        pass

    @abstractmethod
    def notifySubscriber():
        pass

class YoutubeChannelImpl(SocialChannel):
    def __init__(self, name: str):
        self.subscribers: list[Subscriber] = []
        self.name = name

    def addSubscriber(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)
        print(f"Added {subscriber.name} to {self.name} channel")

    def removeSubscriber(self, subscriber: Subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
            print(f"Removed {subscriber.name} from {self.name} channel")
        else:
            print("Invalid Subscriber")

    def notifySubscriber(self, video: str):
        for s in self.subscribers:
            s.update(video)

class TwitchChannelImpl(SocialChannel):
    def __init__(self, name: str):
        self.subscribers: list[Subscriber] = []
        self.name = name

    def addSubscriber(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)
        print(f"Added {subscriber.name} to {self.name} channel")

    def removeSubscriber(self, subscriber: Subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
            print(f"Removed {subscriber.name} from {self.name} channel")
        else:
            print("Invalid Subscriber")

    def notifySubscriber(self, video: str):
        for s in self.subscribers:
            s.update(video)
    
def main():
    user1 = YoutubeSubscriber("User1")
    user2 = YoutubeSubscriber("User2")
    user3 = EmailSubscriber("User3")
    user4 = YoutubeSubscriber("User4")
    user5 = PushSubscriber("User5")

    music_channel = YoutubeChannelImpl("Music")
    sport_channel = YoutubeChannelImpl("Sport")
    news_channel = TwitchChannelImpl("News")
    

    music_channel.addSubscriber(user1)
    music_channel.addSubscriber(user3)

    sport_channel.addSubscriber(user1)
    sport_channel.addSubscriber(user2)
    sport_channel.addSubscriber(user4)
    sport_channel.addSubscriber(user5)

    news_channel.addSubscriber(user3)

    music_channel.notifySubscriber("Local Train")
    music_channel.notifySubscriber("YOYOYO")

    sport_channel.notifySubscriber("F1")
    
    sport_channel.removeSubscriber(user4)
    music_channel.removeSubscriber(user4)

    sport_channel.notifySubscriber("Ind vs Pak")

    news_channel.notifySubscriber("247 News")

if __name__ == "__main__":
    main()
