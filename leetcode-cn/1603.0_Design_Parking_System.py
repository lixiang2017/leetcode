'''
Time: O(1)
Space: O(1)

执行用时：616 ms, 在所有 Python 提交中击败了5.61%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了73.83%的用户
'''


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.slots = [big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.slots[carType - 1] > 0:
            self.slots[carType - 1] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
