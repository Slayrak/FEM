class Cube:
    def __init__(self, cube_number, vertices=[]):
        self._cube_number = cube_number
        self._vertices = vertices

    @property
    def cube_number(self):
        return self._cube_number

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, value):
        self._vertices = value