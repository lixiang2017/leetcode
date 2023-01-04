'''
hash table

Runtime: 2787 ms, faster than 14.27% of Python3 online submissions for Minimum Rounds to Complete All Tasks.
Memory Usage: 28.6 MB, less than 31.64% of Python3 online submissions for Minimum Rounds to Complete All Tasks.
'''
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        ans = 0
        for d, cnt in c.items():
            if cnt == 1:
                return -1
            ans += (cnt + 2) // 3
        return ans
        

'''
Runtime: 2145 ms, faster than 44.59% of Python3 online submissions for Minimum Rounds to Complete All Tasks.
Memory Usage: 28.5 MB, less than 44.10% of Python3 online submissions for Minimum Rounds to Complete All Tasks.
'''
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        ans = 0
        for cnt in c.values():
            if cnt == 1:
                return -1
            ans += (cnt + 2) // 3
        return ans
        
        