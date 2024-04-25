class Vector:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y+other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

U = Vector(1,-1)
V = Vector(2,1)
H = U+V
I = U-V
print("Addition: ", H.x, H.y)
print("Substraction: ", I.x, I.y)