class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        """create a d dimensional vector of zeros"""
        self.__coords = [0] *d

    def __len__(self):
        """Return dimension of the vector"""
        return len(self.__coords)

    def __getitem__(self, j):
        """Return the jth coordinate of the vector"""
        return self.__coords[j]

    def __setitem__(self, j, val):
        """set jth coordinate value to val"""
        self.__coords[j] = val

    def  __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):         # relies on _len__ method
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))      #start with vector of zeros (Final vector)
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has the same coordinates as other"""
        return self.__coords == other.__coords

    def __ne__(self, other):
        """Return True if vector differs from other"""
        return not self == other               # rely on existing __eq__ definition

    def __str__(self):
        """Produce String representation of our vector"""
        return '<' + str(self.__coords)[1:-1] + '>' #adapt list representation







v = Vector(5)   #construct a five dimensional<0,0,0,0,0,>
v[1]=23         #<0,23,0,0,0> based on use of __setitem__
v[-1]=45        #<0,23,0,0,45> based on use of __setitem__
print(v[4])     #print 45 based on __getitem__
u =v+v          #<0,46,0,0,90> via __add__
print(u)
total = 0
for entry in v:
    total += entry             #implicit iteration via __len__ and __getitem__