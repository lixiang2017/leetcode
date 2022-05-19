class X:
    
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return 'this is X: ' + str(self.num)

    def __add__(self, other):
        return self.num + other.num
    
    __radd__ = __add__


class Y:

    def __init__(self, num):
        self.num = num

    def __str__(self):
        return 'this is Y: ' +  str(self.num)


x = X(5)
y = Y(10)
#
print(x)
print(y)

print(x+y)
print(y+x)
#
#
z = x + y 
print(type(x), type(y), type(z))
print(str(z))


'''
this is X: 5
this is Y: 10
15
15
(<type 'instance'>, <type 'instance'>, <type 'int'>)
15
'''