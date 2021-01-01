'''
You are here!
Your runtime beats 77.27 % of python submissions.
'''

from math import ceil, log

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        times = minutesToTest // minutesToDie + 1
        return int(ceil(log(buckets, times)))

        # return ceil(log(buckets, times))  # 5.0



'''
from math import ceil

Help on built-in function ceil in module math:

ceil(...)
    ceil(x)

    Return the ceiling of x as a float.
    This is the smallest integral value >= x.
'''


'''
from math import log

Help on built-in function log in module math:

log(...)
    log(x[, base])

    Return the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x.
'''




'''
Help on class int in module __builtin__:

class int(object)
 |  int(x=0) -> int or long
 |  int(x, base=10) -> int or long
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is floating point, the conversion truncates towards zero.
 |  If x is outside the integer range, the function returns a long instead.
 |
 |  If x is not a number or if base is given, then x must be a string or
 |  Unicode object representing an integer literal in the given base.  The
 |  literal can be preceded by '+' or '-' and be surrounded by whitespace.
 |  The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
 |  interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Methods defined here:
 |
 |  __abs__(...)
 |      x.__abs__() <==> abs(x)
 |
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |
 |  __and__(...)
 |      x.__and__(y) <==> x&y
 |
 |  __cmp__(...)
 |      x.__cmp__(y) <==> cmp(x,y)
 |
 |  __coerce__(...)
 |      x.__coerce__(y) <==> coerce(x, y)
 |
 |  __div__(...)
 |      x.__div__(y) <==> x/y
 |
 |  __divmod__(...)
 |      x.__divmod__(y) <==> divmod(x, y)
 |
 |  __float__(...)
 |      x.__float__() <==> float(x)
 |
 |  __floordiv__(...)
 |      x.__floordiv__(y) <==> x//y
 |
 |  __format__(...)
 |
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |
 |  __getnewargs__(...)
 |
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |
 |  __hex__(...)
 |      x.__hex__() <==> hex(x)
 |
 |  __index__(...)
 |      x[y:z] <==> x[y.__index__():z.__index__()]
 |
 |  __int__(...)
 |      x.__int__() <==> int(x)
 |
 |  __invert__(...)
 |      x.__invert__() <==> ~x
 |
 |  __long__(...)
 |      x.__long__() <==> long(x)
 |
 |  __lshift__(...)
 |      x.__lshift__(y) <==> x<<y
 |
 |  __mod__(...)
 |      x.__mod__(y) <==> x%y
 |
 |  __mul__(...)
 |      x.__mul__(y) <==> x*y
 |
 |  __neg__(...)
 |      x.__neg__() <==> -x
 |
 |  __nonzero__(...)
 |      x.__nonzero__() <==> x != 0
 |
 |  __oct__(...)
 |      x.__oct__() <==> oct(x)
 |
 |  __or__(...)
 |      x.__or__(y) <==> x|y
 |
 |  __pos__(...)
 |      x.__pos__() <==> +x
 |
 |  __pow__(...)
 |      x.__pow__(y[, z]) <==> pow(x, y[, z])
 |
 |  __radd__(...)
 |      x.__radd__(y) <==> y+x
 |
 |  __rand__(...)
 |      x.__rand__(y) <==> y&x
 |
 |  __rdiv__(...)
 |      x.__rdiv__(y) <==> y/x
 |
 |  __rdivmod__(...)
 |      x.__rdivmod__(y) <==> divmod(y, x)
 |
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |
 |  __rfloordiv__(...)
 |      x.__rfloordiv__(y) <==> y//x
 |
 |  __rlshift__(...)
 |      x.__rlshift__(y) <==> y<<x
 |
 |  __rmod__(...)
 |      x.__rmod__(y) <==> y%x
 |
 |  __rmul__(...)
 |      x.__rmul__(y) <==> y*x
 |
 |  __ror__(...)
 |      x.__ror__(y) <==> y|x
 |
 |  __rpow__(...)
 |      y.__rpow__(x[, z]) <==> pow(x, y[, z])
 |
 |  __rrshift__(...)
 |      x.__rrshift__(y) <==> y>>x
 |
 |  __rshift__(...)
 |      x.__rshift__(y) <==> x>>y
 |
 |  __rsub__(...)
 |      x.__rsub__(y) <==> y-x
 |
 |  __rtruediv__(...)
 |      x.__rtruediv__(y) <==> y/x
 |
 |  __rxor__(...)
 |      x.__rxor__(y) <==> y^x
 |
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |
 |  __sub__(...)
 |      x.__sub__(y) <==> x-y
 |
 |  __truediv__(...)
 |      x.__truediv__(y) <==> x/y
 |
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |
 |  __xor__(...)
 |      x.__xor__(y) <==> x^y
 |
 |  bit_length(...)
 |      int.bit_length() -> int
 |
 |      Number of bits necessary to represent self in binary.
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  denominator
 |      the denominator of a rational number in lowest terms
 |
 |  imag
 |      the imaginary part of a complex number
 |
 |  numerator
 |      the numerator of a rational number in lowest terms
 |
 |  real
 |      the real part of a complex number
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

'''



