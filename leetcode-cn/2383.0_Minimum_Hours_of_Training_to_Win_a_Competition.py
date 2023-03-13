'''
执行用时：36 ms, 在所有 Python3 提交中击败了72.59% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了71.11% 的用户
通过测试用例：111 / 111
'''
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        training = 0
        for eng, exp in zip(energy, experience):
            if initialEnergy > eng:
                initialEnergy -= eng 
            else:
                training += eng + 1 - initialEnergy
                initialEnergy = 1

            if initialExperience > exp:
                initialExperience += exp
            else:
                training += exp + 1 - initialExperience
                initialExperience = exp * 2 + 1

        return training
        