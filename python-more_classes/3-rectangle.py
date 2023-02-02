#!/usr/bin/python3
""" rectangle """


class Rectangle():
    """ rectangle """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            Rectangle = ""
            for k in range(0, self.height):
                for j in range(0, self.width):
                    Rectangle += "#"
                Rectangle += "\n"
            return Rectangle
