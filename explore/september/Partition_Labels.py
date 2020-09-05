'''
You are here!
Your runtime beats 59.82 % of python submissions.
'''



class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = [0] * 26
        for i in range(len(S)):
        	last[ord(S[i]) - ord('a')] = i

        result = []
        start, end = 0, 0
        for i in range(len(S)):
        	end = max(end, last[ord(S[i]) - ord('a')])
        	if i == end:   # all the characters of current partition included
        		result.append(i - start + 1)
        		start = i + 1
        return result




if __name__ == '__main__':
	S = "ababcbacadefegdehijhklij"
	assert Solution().partitionLabels(S) == [9,7,8]