'''
执行用时：28 ms, 在所有 Python3 提交中击败了98.26% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了71.37% 的用户
'''
class Solution:
    def maximum(self, a: int, b: int) -> int:
        return max(a, b)


'''
执行用时：28 ms, 在所有 Python3 提交中击败了98.26% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了26.46% 的用户
'''
class Solution:
    def maximum(self, a: int, b: int) -> int:
        return (a + b + abs(a - b)) // 2



'''
ref:
https://leetcode-cn.com/problems/maximum-lcci/solution/li-yong-shu-xue-si-wei-de-fang-fa-by-nhan/

/*
作者：OrangeMan
链接：https://leetcode-cn.com/problems/maximum-lcci/solution/cjian-ji-dai-ma-by-orangeman-22/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/

'''
class Solution:
    def maximum(self, a: int, b: int) -> int:
        return (a + b + self.absolute(a - b)) // 2
    
    def absolute(self, x):
        flag = x >> 63    # 正数flag = 0，负数flag = -1
        return (flag ^ x) - flag   # 任何数与0异或值不变，任何数与-1异或等价于按位取反


