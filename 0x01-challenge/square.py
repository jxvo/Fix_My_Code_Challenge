#!/usr/bin/python3
"""
square module
"""


class square():
""" Square class """

    def __init__(self, *args, **kwargs):
    """ Initialize attrs """
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimerter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns formatted attrs """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
