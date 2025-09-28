from abc import ABC, abstractmethod
import random

class PlaylistIterator(ABC):
    @abstractmethod
    def hasNext(self, idx) -> bool:
        pass
    
    @abstractmethod
    def playNext(self) -> str:
        pass

class Playlist():
    def __init__(self):
        self.songs: list[str] = []
    
    def addSong(self, song: str):
        if song not in self.songs:
            self.songs.append(song)

    def getSong(self, idx: int) -> str:
        return self.songs[idx]


class SimplePlaylistIterator(PlaylistIterator):

    def __init__(self, playlist: Playlist):
        self.playlist = playlist
        self.index = -1

    def hasNext(self) -> bool:
        print(self.index + 1 < len(self.playlist.songs))
        return self.index + 1 < len(self.playlist.songs)
    
    def playNext(self) -> str:
        if self.hasNext():
            self.index += 1
            song = self.playlist.getSong(self.index)
            print("Playing", song)
            return song
        else:
            print("Played full playlist.")
            return ""
        
    
class ShufflePlaylistIterator(PlaylistIterator):

    def __init__(self, playlist: Playlist):
        self.songs = playlist.songs[:]
        random.shuffle(self.songs)
        self.index = -1

    def hasNext(self) -> bool:
        print(self.index + 1 < len(self.songs))
        return self.index + 1 < len(self.songs)
    
    def playNext(self) -> str:
        if self.hasNext():
            self.index += 1
            song = self.songs[self.index]
            print("Playing", song)
            return song
        else:
            print("Played full playlist.")
            return ""
    
def main():
    playlist = Playlist()
    playlist.addSong("song 1")
    playlist.addSong("song 2")
    playlist.addSong("song 3")
    playlist.addSong("song 4")
    playlist.addSong("song 5")

    pi = SimplePlaylistIterator(playlist)
    pi.hasNext()
    pi.playNext()
    pi.playNext()
    pi.playNext()
    pi.playNext()
    pi.playNext()
    pi.playNext()

    spi = ShufflePlaylistIterator(playlist)
    spi.hasNext()
    spi.playNext()
    spi.playNext()
    spi.playNext()
    spi.playNext()
    spi.playNext()

if __name__ == "__main__":
    main()
    