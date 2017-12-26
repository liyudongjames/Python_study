# 歌曲父类


class Song(object):
    def __init__(self, lyrics):
        self.__lyrics = lyrics

    def sing(self):
        print(self.__lyrics)
