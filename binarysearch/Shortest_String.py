'''
Success!
Your code took 47 milliseconds — faster than 53.85% in Python
'''
class Solution:
    def solve(self, s):
        c = Counter(s)
        return abs(c['1'] - c['0'])
