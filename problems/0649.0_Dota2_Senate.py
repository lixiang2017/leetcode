'''
deque + deque
T: O(N)
S: O(N)

Runtime: 70 ms, faster than 48.62% of Python3 online submissions for Dota2 Senate.
Memory Usage: 16.8 MB, less than 5.50% of Python3 online submissions for Dota2 Senate.
'''
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()
        
        return 'Radiant' if radiant else 'Dire'
