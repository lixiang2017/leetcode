'''
You are here!
Your runtime beats 31.46 % of python submissions.
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = {'1': '1', '2': '11'}
        
        if 1 == n:
            return "1"
        elif 2 == n:
            return "11"
        if str(n - 1) in say:
            n_1 = say[str(n - 1)]
        else:    
            n_1 = self.countAndSay(n - 1)
            say[str(n - 1)] = n_1
            print 'n_1: ', n - 1, 
            print 'say: ', say[str(n - 1)]
        size = len(n_1)
        res = ''
        # current_char = n_1[0]
        current_count = 0
        for i in xrange(size - 1):
            current_char = n_1[i]
            if n_1[i] == n_1[i + 1]:
                current_count += 1
                if i == size - 2:
                    res += str(current_count + 1)
                    res += current_char                    
            else:
                res += str(current_count + 1)
                res += current_char
                if i == size - 2:
                    res += '1'
                    res += n_1[-1]   
                current_count = 0
        
        return res
