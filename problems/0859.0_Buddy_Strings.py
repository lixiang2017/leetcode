'''
Runtime: 51 ms, faster than 49.59% of Python3 online submissions for Buddy Strings.
Memory Usage: 16.5 MB, less than 66.33% of Python3 online submissions for Buddy Strings.
'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        cnt1, cnt2 = Counter(s), Counter(goal)
        if cnt1 != cnt2:
            return False
        if s == goal:
            return max(cnt1.values()) > 1
        diff = [[a, b] for a, b in zip(s, goal) if a != b]
        return 2 == len(diff) and diff[0] == diff[1][:: -1]

'''
Runtime: 49 ms, faster than 62.96% of Python3 online submissions for Buddy Strings.
Memory Usage: 16.6 MB, less than 28.16% of Python3 online submissions for Buddy Strings.
'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        cnt1, cnt2 = Counter(s), Counter(goal)
        if cnt1 != cnt2:
            return False
        if s == goal:
            return max(cnt1.values()) > 1
        diff = [ord(a) - ord(b) for a, b in zip(s, goal) if a != b]
        return 2 == len(diff) and 0 == sum(diff)
