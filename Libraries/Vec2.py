

from math import sqrt

class Vec2:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        if type(x) == tuple:
            self.x = x[0]
            self.y = x[0]

            if y != 0:
                raise ValueError("Tuple and other supplied")
        
        else:
            self.x = x
            self.y = y
    
    def __add__(self, other: object):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other: object):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: object):
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __isub__(self, other: object):
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __mul__(self, other: float):
        return Vec2(self.x * other, self.y * other)
    
    def __imul__(self, other: float):
        self.x *= other
        self.y *= other
        return self
    
    def __truediv__(self, other: float):
        return Vec2(self.x / other, self.y / other)
    
    def __itruediv__(self, other: float):
        self.x /= other
        self.y /= other
        return self

    def lenght(self):
        return sqrt(self.x * self.x + self.y * self.y)
    
    def square_dist(self, other: object):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2
    
    def dist(self, other: object):
        return sqrt(self.square_dist(other))

    def norm(self):
        return self / self.lenght()

    def norm_inline(self):
        self /= self.lenght()

    def dot(self, other: object):
        return self.x * other.x + self.y * other.y

    def tuple(self):
        return (self.x, self.y)

    def __getitem__(self, key: int):
        if not isinstance(key, int):
            raise TypeError("Key mist be int")
        
        if key > 1:
            raise IndexError("Key can not be bigger than 1 for Vec2")
        
        if key == 0: return self.x
        elif key == 1: return self.y
        else:
            raise KeyError("Something wrong")

    def __str__(self) -> str:
        return f"x = {self.x} | y = {self.y}"
    
    def __format__(self, specification):
        if specification == ".2":
            return f"x = {self.x :.2} | y = {self.y :.2}"
        
        else:
            return f"x = {self.x} | y = {self.y}"

    def __repr__(self) -> str:
        return self.__str__()
    
    def __iter__(self):
        return iter((self.x, self.y))
    
    def __ne__(self, __value: object) -> bool:
        return ((self.x != __value.x) or (self.y != __value.y))
