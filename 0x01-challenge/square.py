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
        elif self.height != 0:
            self.width = self.height

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter(self):
        """ Perrr """
        return (self.width * 4)

    def __str__(self):
        """ STR """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ Main """
    s = Square(width=12, height=12)
    print(s)
    print(s.area())
    print(s.perimeter())
    t = Square(height=2)
    print(t)
    print(t.area())
    print(t.perimeter())
