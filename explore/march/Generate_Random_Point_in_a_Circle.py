'''
You are here!
Your runtime beats 94.12 % of python submissions.
You are here!
Your memory usage beats 82.35 % of python submissions.
'''



from math import sin, cos, pi, sqrt
from random import random

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        radians = random() * pi * 2
        l = self.radius * sqrt(random())
        return [
            self.x_center + l * cos(radians),
            self.y_center + l * sin(radians)            
        ]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
