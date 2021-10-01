'''
You are here!
Your runtime beats 53.54 % of python3 submissions.

'''

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        do = ''
        while do != dominoes:
            do = dominoes
            dominoes = dominoes.replace('R.L', 'T')
            dominoes = dominoes.replace('.L', 'LL')
            dominoes = dominoes.replace('R.', 'RR')
            dominoes = dominoes.replace('T', 'R.L')
        return dominoes



'''
You are here!
Your runtime beats 50.92 % of python3 submissions.
You are here!
Your memory usage beats 99.74 % of python3 submissions
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        do = ''
        while do != dominoes:
            do = dominoes
            dominoes = dominoes.replace('R.L', 'T').replace('.L', 'LL').replace('R.', 'RR').replace('T', 'R.L')
        return dominoes
