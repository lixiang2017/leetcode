'''
AC

219 / 219 个通过测试用例
状态：通过
执行用时: 124 ms
内存消耗: 20.1 MB
提交时间：3 小时前
'''
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def compare(a: str, b: str):
            if len(a) > len(b):
                return 1
            elif len(a) < len(b):
                return -1
            else:
                if a > b:
                    return 1
                elif a < b:
                    return -1
                else:
                    return 0
            
        s = sorted(nums, key=functools.cmp_to_key(compare), reverse=True)
        return s[k - 1]



'''
执行用时：72 ms, 在所有 Python3 提交中击败了66.67% 的用户
内存消耗：20.1 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：219 / 219
'''
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return sorted(nums, key=int)[-k]
        