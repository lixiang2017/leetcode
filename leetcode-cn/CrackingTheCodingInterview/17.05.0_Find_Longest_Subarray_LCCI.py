'''
prefix sum + hash table
最长子数组
转换数字为 1，字母为 -1
数字字母个数相等，即为子数组和为 0。
哈希表记录之前出现前缀和的下标，当计算出现之前出现过的前缀和，更新结果即可。

T: O(N)
S: O(N)

执行用时：120 ms, 在所有 Python3 提交中击败了92.63% 的用户
内存消耗：32.3 MB, 在所有 Python3 提交中击败了40.00% 的用户
通过测试用例：45 / 45
'''
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        pre = 0
        index = {0: -1}
        left = len(array)
        subarray_len = 0
        for i, ch in enumerate(array):
            if ch.isdigit():
                pre += 1
            else:
                pre -= 1
            if pre in index:
                idx = index[pre]
                cur_len = i - idx
                if cur_len > subarray_len or (cur_len == subarray_len and left > idx + 1):
                    left = idx + 1
                    subarray_len = cur_len
            else:
                index[pre] = i
                
        if subarray_len > 0:
            return array[left: left + subarray_len]
        else:
            return []

'''
执行用时：116 ms, 在所有 Python3 提交中击败了95.79% 的用户
内存消耗：32.4 MB, 在所有 Python3 提交中击败了40.00% 的用户
通过测试用例：45 / 45
'''
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        pre = 0
        index = {0: -1}
        left = len(array)
        subarray_len = 0
        for i, ch in enumerate(array):
            if ch.isdigit():
                pre += 1
            else:
                pre -= 1
            if pre in index:
                idx = index[pre]
                cur_len = i - idx
                if cur_len > subarray_len:
                    left = idx + 1
                    subarray_len = cur_len
            else:
                index[pre] = i
                        
        return array[left: left + subarray_len] if subarray_len > 0 else []

