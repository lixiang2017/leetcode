'''
You are here!
Your runtime beats 61.90 % of python submissions.
'''



class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B = 0, 0
        secret_b, guess_b = [], []
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                secret_b.append(secret[i])
                guess_b.append(guess[i])
        
        secret_dict = collections.Counter(secret_b)
        guess_dict = collections.Counter(guess_b)
        for i, i_value in secret_dict.iteritems():
            for j, j_value in guess_dict.iteritems():
                if i == j:
                    B += min(i_value, j_value)
        
        return str(A) + 'A' + str(B) + 'B'
