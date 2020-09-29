#!/usr/bin/python3


class Square():
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if self.width == self.height:
            self.size = self.width

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def PermiterOfMySquare(self):
        return (self.size * 4)

    def __str__(self):
        return "{}".format(self.size)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
