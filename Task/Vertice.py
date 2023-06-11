class Vertice:
    def __init__(self, outer_number, inner_number=0, coords=[]):
        self._inner_number = inner_number
        self._outer_number = outer_number
        self._coords = coords

    @property
    def inner_number(self):
        return self._inner_number

    @property
    def outer_number(self):
        return self._outer_number

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, value):
        self._coords = value

    @inner_number.setter
    def inner_number(self, value):
        self._inner_number = value

    def __eq__(self, other):
        return isinstance(other, Vertice) and self.coords == other.coords