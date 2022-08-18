'''
hash table + sort 

Runtime: 865 ms, faster than 65.18% of Python3 online submissions for Reduce Array Size to The Half.
Memory Usage: 37.7 MB, less than 24.52% of Python3 online submissions for Reduce Array Size to The Half.
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c, n = Counter(arr), len(arr)
        occurences = sorted([[cnt, k] for k, cnt in c.items()], reverse=True)
        ans = delete = 0
        for cnt, k in occurences:
            delete += cnt
            ans += 1
            if delete >= n - delete:
                return ans
        return -1


'''
Runtime: 1075 ms, faster than 34.81% of Python3 online submissions for Reduce Array Size to The Half.
Memory Usage: 31.7 MB, less than 86.40% of Python3 online submissions for Reduce Array Size to The Half.
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c, n = Counter(arr), len(arr)
        occurences = sorted([cnt for k, cnt in c.items()], reverse=True)
        ans = delete = 0
        for cnt in occurences:
            delete += cnt
            ans += 1
            if delete >= n - delete:
                return ans
        return -1
