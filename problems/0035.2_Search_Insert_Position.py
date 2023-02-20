'''
Solution: bisect module
Author: lixiang

bisect模块提供的函数有：

bisect.bisect_left(a, x, lo=0, hi=len(a)) :
查找在有序列表 a 中插入 x 的index。lo 和 hi 用于指定列表的区间，默认是使用整个列表。如果 x 已经存在，在其左边插入。返回值为 index。

bisect.bisect_right(a, x, lo=0, hi=len(a))
bisect.bisect(a, x,lo=0, hi=len(a)) ：
这2个函数和 bisect_left 类似，但如果 x 已经存在，在其右边插入。

bisect.insort_left(a,x, lo=0, hi=len(a)) ：
在有序列表 a 中插入 x。和 a.insert(bisect.bisect_left(a, x, lo, hi), x) 的效果相同。

bisect.insort_right(a,x, lo=0, hi=len(a))
bisect.insort(a, x,lo=0, hi=len(a)) :
和 insort_left 类似，但如果 x 已经存在，在其右边插入。

bisect 模块提供的函数可以分两类： bisect* 只用于查找 index， 不进行实际的插入；而 insort* 则用于实际插入
'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        return bisect.bisect_left(nums, target)


if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    print(Solution().searchInsert(nums, target))

    target = 2
    print(Solution().searchInsert(nums, target))

    target = 7
    print(Solution().searchInsert(nums, target))

    target = 0
    print(Solution().searchInsert(nums, target))