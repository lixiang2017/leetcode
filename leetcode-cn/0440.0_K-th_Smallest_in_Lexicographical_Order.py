'''
执行用时：48 ms, 在所有 Python3 提交中击败了5.36% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了70.36% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_count(prefix: int, n: int) -> int:
            count = 0
            cur = prefix
            next_ = prefix + 1
            while cur <= n:
                count += min(next_, n + 1) - cur 
                cur *= 10
                next_ *= 10

            return count 

        p = 1 
        prefix = 1 
        while p < k:
            cnt = get_count(prefix, n)
            if p + cnt > k:
                prefix *= 10 
                p += 1 
            elif p + cnt <= k:
                prefix += 1
                p += cnt 
                
        return prefix 


'''
执行用时：44 ms, 在所有 Python3 提交中击败了12.36% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了79.67% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1

        while k:
            left, right = cur, cur + 1
            node_cnt = 0
            while left <= n:
                node_cnt += min(right, n + 1) - left
                left *= 10
                right *= 10
            
            if node_cnt <= k:
                cur += 1
                k -= node_cnt
            else:
                cur *= 10
                k -= 1

        return cur 
        