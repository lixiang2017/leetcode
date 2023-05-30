'''
Runtime: 137 ms, faster than 62.17% of Python3 online submissions for Design Parking System.
Memory Usage: 16.9 MB, less than 15.89% of Python3 online submissions for Design Parking System.
'''
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.slots[carType - 1] -= 1
        return self.slots[carType - 1] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
