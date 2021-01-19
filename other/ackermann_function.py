'''
https://en.wikipedia.org/wiki/Ackermann_function
https://www.geeksforgeeks.org/ackermann-function/


A(0, n) = n + 1
A(m, 0) = A(m - 1, 1) 
A(m, n) = A(m - 1, A(m, n - 1))

'''

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

m = int(input("please enter m: "))
n = int(input("please enter n: "))
print("ackermann({}, {}) is {}".format(m, n, ackermann(m, n)))

