'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3434/

Python2 Time Limit Exceeded
Python3 Accepted	
	You are here!
	Your runtime beats 51.02 % of python3 submissions.
'''


class StreamChecker:
    # Trie version
    def __init__(self, words: List[str]):
        self.Trie={}
        for word in words:
            curnode=self.Trie
            word=word[::-1]
            for ch in word:
                if ch not in curnode:
                    curnode[ch]={}
                curnode=curnode[ch]
            curnode['#']=1 # '#' means the end of a word
        self.pre=''

    def query(self, letter: str) -> bool:
        self.pre=self.pre+letter
        curnode=self.Trie
        for i in range(0,len(self.pre)):
            if self.pre[-i-1] not in curnode:
                break
            curnode=curnode[self.pre[-i-1]]
            if '#' in curnode:
                return True
        return False    


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


if __name__ == '__main__':
	words = ["cd","f","kl"]
	# StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
	streamChecker = StreamChecker(["cd","f","kl"])
	assert not streamChecker.query('a')     #     // return false
	assert not streamChecker.query('b')     #     // return false
	assert not streamChecker.query('c')     #     // return false
	assert streamChecker.query('d')         # // return true, because 'cd' is in the wordlist
	assert not streamChecker.query('e')     #     // return false
	assert streamChecker.query('f')         # // return true, because 'f' is in the wordlist
	assert not streamChecker.query('g')     #     // return false
	assert not streamChecker.query('h')     #     // return false
	assert not streamChecker.query('i')     #     // return false
	assert not streamChecker.query('j')     #     // return false
	assert not streamChecker.query('k')     #     // return false
	assert streamChecker.query('l')         # // return true, because 'kl' is in the wordlist

