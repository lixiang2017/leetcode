'''
Question 735 of 1037

Success!
Your code took 100 milliseconds — faster than 91.00% in Python
'''
class Trie:
    def __init__(self):
        self.t = dict()

    def add(self, s):
        t = self.t 
        for ch in s:
            if ch not in t:
                t[ch] = dict()
            t = t[ch]
        t['#'] = True

    def exists(self, word):
        t = self.t 
        for ch in word:
            if ch not in t:
                return False 
            t = t[ch]
        return '#' in t 

    def startswith(self, p):
        t = self.t 
        for ch in p:
            if ch not in t:
                return False 
            t = t[ch]  
        return True     
