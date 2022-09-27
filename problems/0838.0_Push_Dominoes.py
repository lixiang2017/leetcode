'''
left force and right force, check which one is more powerful.
T: O(3N)
S: O(2N)

Runtime: 293 ms, faster than 86.68% of Python3 online submissions for Push Dominoes.
Memory Usage: 17.9 MB, less than 55.84% of Python3 online submissions for Push Dominoes.
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n, ans = len(dominoes), list(dominoes)
        l_force, r_force = [0] * n, [0] * n
        # from right to left
        L = None
        for i in range(n - 1,  -1, -1):
            if dominoes[i] == 'L':
                L = -1
            elif dominoes[i] == 'R':
                L = None
            elif L is not None:
                L -= 1
                l_force[i] = L 
        # from left to right
        R = None 
        for i in range(n):
            if dominoes[i] == 'L':
                R = None
            elif dominoes[i] == 'R':
                R = 1
            elif R is not None:
                R += 1
                r_force[i] = R
        
        # check l_force and r_force
        for i in range(n):
            if dominoes[i] == '.' and -l_force[i] != r_force[i]:
                if 0 == l_force[i]:
                    ans[i] = 'R'
                elif 0 == r_force[i]:
                    ans[i] = 'L'
                else:
                    ans[i] = ['L', 'R'][-l_force[i] > r_force[i]]

        return ''.join(ans)
        
