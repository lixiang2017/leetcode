'''
Success
Details 
Runtime: 88 ms, faster than 54.21% of Python online submissions for Top K Frequent Elements.
Memory Usage: 16.9 MB, less than 33.22% of Python online submissions for Top K Frequent Elements.
'''


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = collections.Counter(nums)
        hashmap = sorted(hashmap.iteritems(), key = lambda item: item[1], reverse = True)
        
        topk = []
        for i in range(k):
            topk.append(hashmap[i][0])
        return topk
