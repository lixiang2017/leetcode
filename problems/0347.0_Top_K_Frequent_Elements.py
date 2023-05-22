'''
sort 
T: O(N + NlogN + k)
S: O(N + logN + k)

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


'''
max heap for all 
T: O(N + N + N + klogN)
S: O(N + N)
大根堆（python频次存负数）要存储所有数字的频次

Runtime: 127 ms, faster than 63.61% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.9 MB, less than 19.84% of Python3 online submissions for Top K Frequent Elements.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        h = [(-f, x) for x, f in freq.items()]
        heapify(h)
        return [x for neg_f, x in nsmallest(k, h)]


'''
小根堆只需存储k个频次最高的即可。
但是从小根堆的最后输出，不是频次降序的。如果需要频次降序，需要重新排序k。
min heap for k
T: O(N + N + Nlogk)
S: O(N + k)

Runtime: 110 ms, faster than 82.25% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.6 MB, less than 68.16% of Python3 online submissions for Top K Frequent Elements.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        h = []
        for x, f in freq.items():
            if len(h) >= k and h[0][0] >= f:
                continue
            # if not h or f > h[0][0]:
            heappush(h, (f, x))
            if len(h) > k:
                heappop(h)

        # output, not sorted for freq      
        return [x for f, x in h]

'''
min heap for k
T: O(N + N + Nlogk + klogk)
S: O(N + k)

Runtime: 116 ms, faster than 75.86% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.6 MB, less than 91.71% of Python3 online submissions for Top K Frequent Elements.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        h = []
        for x, f in freq.items():
            if len(h) >= k and h[0][0] >= f:
                continue
            heappush(h, (f, x))
            if len(h) > k:
                heappop(h)
        
        # output, descreasing in freq
        ans = [0] * k
        for i in range(k - 1, -1, -1):
            ans[i] = heappop(h)[1]
        return ans


'''
Runtime: 165 ms, faster than 32.32% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.6 MB, less than 91.71% of Python3 online submissions for Top K Frequent Elements.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        freq = Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=freq.get)


'''
Runtime: 150 ms, faster than 43.64% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.6 MB, less than 91.71% of Python3 online submissions for Top K Frequent Elements.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        freq = Counter(nums)
        return nlargest(k, freq.keys(), key=freq.get)


'''
Runtime: 119 ms, faster than 34.88% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 21.2 MB, less than 30.27% of Python3 online submissions for Top K Frequent Elements.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return nlargest(k, cnt := Counter(nums), key=lambda x: cnt[x])

'''
Runtime: 119 ms, faster than 34.88% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 21.1 MB, less than 41.02% of Python3 online submissions for Top K Frequent Elements.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return nsmallest(k, freq := Counter(nums), key=lambda x: -freq[x])
