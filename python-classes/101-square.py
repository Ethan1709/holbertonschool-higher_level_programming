#!/usr/bin/python3
""" square """


class Square:
    """ square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(self.position[1]):
            print()
        for i in range(0, self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for n in range(0, self.size):
                print("#", end="")
            print()

    def __str__(self):
        square = ""
        if self.size == 0:
            square = ""
        for i in range(self.position[1]):
            square += ('\n')
        for i in range(0, self.size):
            for j in range(self.position[0]):
                square += " "
            for n in range(0, self.size):
                square += "#"
            square += ('\n')
        return square[:-1]

        
