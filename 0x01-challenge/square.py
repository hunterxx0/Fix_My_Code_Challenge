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
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Permit """
        return (self.width * 4)

    def __str__(self):
        """ STR """
        return "{}".format(self.width)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
