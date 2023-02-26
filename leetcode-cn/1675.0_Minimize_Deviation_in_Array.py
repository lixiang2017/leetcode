'''
heap

执行用时：1044 ms, 在所有 Python3 提交中击败了76.67% 的用户
内存消耗：22.4 MB, 在所有 Python3 提交中击败了33.33% 的用户
通过测试用例：75 / 75
'''
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        h = [-(x << 1) if x & 1 else -x for x in nums]
        heapify(h)
        base = max(h)
        ans = base - h[0]
        while h[0] & 1 == 0:
            head = h[0] >> 1
            heapreplace(h, head)
            if head > base:
                base = head 
            ans = min(ans, base - h[0])
        return ans 

