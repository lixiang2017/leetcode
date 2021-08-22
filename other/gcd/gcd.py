
'''
GCD is the largest common divisor that divides the numbers without a remainder.
GCD is also known as the highest common factor (HCF).
'''


from math import gcd

from fractions import gcd

'''
In [11]: from fractions import gcd
In [12]: ??gcd
Signature: gcd(a, b)
Source:   
def gcd(a, b):
    Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    
    import warnings
    warnings.warn('fractions.gcd() is deprecated. Use math.gcd() instead.',
                  DeprecationWarning, 2)
    if type(a) is int is type(b):
        if (b or a) < 0:
            return -math.gcd(a, b)
        return math.gcd(a, b)
    return _gcd(a, b)
File:      /usr/lib/python3.8/fractions.py
Type:      function
'''


'''
math.gcd(a, b)
    Return the greatest common divisor of the integers a and b. If either a or b is nonzero, then the value of gcd(a, b) is the largest positive integer that divides both a and b. gcd(0, 0) returns 0.
    New in version 3.5.
'''


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a


def gcd_recursive(a, b):
	if b == 0:
		return a
	else:
		return gcd_recursive(b, a % b)


gcd = lambda a, b: a if not b else gcd(b, a % b)






