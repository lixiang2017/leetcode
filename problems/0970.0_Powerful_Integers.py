'''
Author: lixiang

64 / 93 test cases passed.
Status: Time Limit Exceeded
'''

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # x = 1, y = 1

        ans = []
        for p in range(bound):
            for  q in range(bound):
                sum = x ** p + y ** q

                if sum <= bound:
                    ans.append(sum)
                elif sum > bound:
                    break 

                if y == 1:
                    break
                
            if x == 1:
                continue

        ans = sorted(list(set(ans)))
        return ans
        
if __name__ == "__main__":
    x = 2
    y = 3
    bound = 10
    assert Solution().powerfulIntegers(x, y, bound) == [2, 3, 4, 5, 7, 9, 10]

    x = 3
    y = 5
    bound = 15
    assert Solution().powerfulIntegers(x, y, bound) == [2, 4, 6, 8, 10, 14]

    x = 1
    y = 1
    bound = 5
    assert Solution().powerfulIntegers(x, y, bound) == [2]

    x = 40
    y = 50
    bound = 10000
    print Solution().powerfulIntegers(x, y, bound)
    # [2, 41, 51, 90, 1601, 1650, 2501, 2540, 4100]
