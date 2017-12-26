# 歌曲子类
from OOP.Song import Song


class I_Am_You(Song):
    def __init__(self):
        super.__init__(self,)

    def sing(self):
        print("Pop music: ")
        super.sing(self)


a_song = I_Am_You("daladaldala")
a_song.sing()