#!/usr/bin/python3
""" Class """


class Square():
    """ Square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Init """
        for key, value in kwargs.items():
            setattr(self, key, value)
        if self.width != 0 and self.width != self.height:
            self.height = self.width
        else:
            self.width = self.height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perrr """
        return (self.width * 4)

    def __str__(self):
        """ STR """
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":
    """ Main """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
