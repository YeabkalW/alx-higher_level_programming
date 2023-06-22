#!/usr/bin/python3
"""defines a class Square that inherits from the Rectangle class since
a square is a rectangle with special features"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """a square class the inherits from Rectangle with special add ons"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the class upon creation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """defines a string to be display when print is called"""
        return "[{}] ({}) {}/{} - {}"\
               .format(type(self).__name__, self.id, self.x, self.y,
                       self.width)

    @property
    def size(self):
        """Retrive the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the height and widht to same value since it a square"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attribute of the class instance"""
        if len(args) == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns a dictionary representation of the class attributes"""
        return {
            'id': int(getattr(self, "id")),
            'x': getattr(self, "x"),
            'size': getattr(self, "size"),
            'y': getattr(self, "y")
        }
