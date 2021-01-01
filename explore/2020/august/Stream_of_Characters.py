'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3434/


query(letter): returns true if and only if for some k >= 1, the last k characters queried \
(in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
'''


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        # last_letters = set()
        for word in self.words:
        	if letter == word[-1]:
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

