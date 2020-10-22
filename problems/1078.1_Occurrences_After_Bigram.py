'''
Success
Details
Runtime: 20 ms, faster than 54.89% of Python online submissions for Occurrences After Bigram.
Memory Usage: 13.6 MB, less than 14.67% of Python online submissions for Occurrences After Bigram.
'''

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split(" ")
        if len(words) < 3:
            return []
        
        result = []
        previous = words[: 2]
        for i in range(2, len(words)):
            if previous[0] == first and previous[1] == second:
                result.append(words[i])
            previous[0] =  previous[1]
            previous[1] = words[i]
        
        return result
