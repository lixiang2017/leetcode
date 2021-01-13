'''
Success
Details 
Runtime: 768 ms, faster than 87.89% of Python online submissions for Count Good Meals.
Memory Usage: 22.4 MB, less than 55.86% of Python online submissions for Count Good Meals.
'''

class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        foodItems = Counter(deliciousness)
        powerOf2 = [2 ** i for i in range(22)]
        
        same_good = diff_good = good = 0
        for deli, cnt in foodItems.iteritems():
            for power in powerOf2:
                if power - deli in foodItems:
                    if deli == power - deli:
                        same_good += cnt * (cnt - 1) / 2
                        same_good %= MOD
                    else:
                        diff_good += cnt * foodItems[power - deli]
                        # diff_good %= MOD

        good = same_good + diff_good / 2
        good %= MOD
        return good