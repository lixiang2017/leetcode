'''
执行用时：36 ms, 在所有 Python3 提交中击败了69.38% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了10.53% 的用户
通过测试用例：109 / 109
'''
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        duration, ans = 0, ''
        for pre, rel, key in zip([0] + releaseTimes, releaseTimes, keysPressed):
            dur = rel - pre 
            if dur > duration or (dur == duration and ord(key) > ord(ans)):
                duration = dur 
                ans = key 

        return ans 

