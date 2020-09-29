#!/usr/bin/python3
""" Square """


class Square():
    """ Square """
    def __init__(self, *args, **kwargs):
        """ init """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        if self.width == self.height:
            return self.width * self.width
        else:
            return 0

    def PermiterOfMySquare(self):
        """ Permit """
        if self.width == self.height:
            return (self.width * 4)
        else:
            return 0

    def __str__(self):
        """ STR """
        if self.width == self.height:
            return "{}".format(self.width)
        else:
            return 0


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
