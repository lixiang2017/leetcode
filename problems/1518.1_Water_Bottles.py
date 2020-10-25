'''
https://leetcode-cn.com/problems/water-bottles/solution/yi-xing-dai-ma-chun-shu-xue-jie-fa-o1-by-dan-yan-l/

淡烟流水画屏幽
（编辑过）2020-07-19
还是解释一下，一个空瓶价值为1的话，numBottles * numExchange为总价值，至少一个空瓶最后留在手里换不了，
所以总价值-1，numExchange-1为一份酒的价值。

https://leetcode-cn.com/problems/water-bottles/solution/huan-jiu-wen-ti-by-leetcode-solution/
方法二：数学
思路与算法

第一步，首先我们一定可以喝到 b 瓶酒，剩下 b 个空瓶。

第二步，接下来我们来考虑空瓶换酒，换完再喝，喝完再换的过程——每次换到一瓶酒就意味着多一个空瓶，
所以每次损失的瓶子的数量为 e−1，我们要知道这个过程能得到多少瓶酒，即希望知道第一个打破下面这个条件的 n 是多少：
b−n(e−1) ≥ e
即我们要找到最小的 n 使得：
b−n(e−1)<e
我们得到 n_{\min} = \lfloor \frac{b - e}{e - 1} + 1\rfloor
当然我们要特别注意这里的前提条件是b≥e，试想如果b<e，没有足够的瓶子再换酒了，就不能进行第二步了。



Success
Details 
Runtime: 20 ms, faster than 51.59% of Python online submissions for Water Bottles.
Memory Usage: 13.5 MB, less than 6.09% of Python online submissions for Water Bottles.

Success
Details 
Runtime: 16 ms, faster than 77.97% of Python online submissions for Water Bottles.
Memory Usage: 13.3 MB, less than 6.09% of Python online submissions for Water Bottles.
'''

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        return (numBottles * numExchange - 1) / (numExchange - 1)
        

'''
Success
Details 
Runtime: 16 ms, faster than 77.97% of Python online submissions for Water Bottles.
Memory Usage: 13.5 MB, less than 6.09% of Python online submissions for Water Bottles.
'''

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        return (numBottles * numExchange - 1) // (numExchange - 1)
        




class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        return numBottles + (numBottles - 1) // (numExchange - 1)
        