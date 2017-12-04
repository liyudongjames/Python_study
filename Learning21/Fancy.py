class Fancy(object):

    @property
    def singer(self):
        return self._singer

    @singer.setter
    def singer(self,value):
        if not isinstance(value, int):
            raise ValueError("必须是一个int类型")
        elif value < 0 or value > 100:
            raise ValueError("必须在1和100之间")
        self._singer = value