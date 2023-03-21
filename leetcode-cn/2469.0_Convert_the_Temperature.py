'''
执行用时：52 ms, 在所有 Python3 提交中击败了5.69% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了29.74% 的用户
通过测试用例：74 / 74
'''
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]

'''
执行用时：40 ms, 在所有 Python3 提交中击败了36.88% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了36.59% 的用户
通过测试用例：74 / 74
'''
class Solution:
    def convertTemperature(self, 摄氏度: float) -> List[float]:
        开氏度 = 摄氏度 + 273.15
        华氏度 = 摄氏度 * 1.80 + 32.00
        return [开氏度, 华氏度]
        