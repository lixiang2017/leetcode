'''
T: O(N)
S: O(1)

You are here!
Your runtime beats 70.22 % of python3 submissions.
'''
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key, duration = keysPressed[0], releaseTimes[0]
        N = len(releaseTimes)
        for i in range(1, N):
            dur = releaseTimes[i] - releaseTimes[i - 1]
            if dur > duration or (dur == duration and keysPressed[i] > key):
                key = keysPressed[i]
                duration = dur
        return key
