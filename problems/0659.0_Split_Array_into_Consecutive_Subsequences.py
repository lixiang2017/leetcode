'''
hash table + priority queue + greedy
T: O(NlogN)
S: O(N)

Runtime: 674 ms, faster than 74.78% of Python3 online submissions for Split Array into Consecutive Subsequences.
Memory Usage: 15.1 MB, less than 99.65% of Python3 online submissions for Split Array into Consecutive Subsequences.
'''
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # num -> min heap (length list ends with num x) 
        x2lens = defaultdict(list)
        for x in nums:
            if q := x2lens[x - 1]:
                cnt = heappop(q)
                heappush(x2lens[x], cnt + 1)
            else:
                heappush(x2lens[x], 1)
        
        return not any(q and q[0] < 3 for q in x2lens.values())
           

'''
hash table + greedy
T: O(2 * N)
S: O(N)

Runtime: 951 ms, faster than 33.98% of Python3 online submissions for Split Array into Consecutive Subsequences.
Memory Usage: 15.2 MB, less than 95.45% of Python3 online submissions for Split Array into Consecutive Subsequences.
'''
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq, end = Counter(nums), Counter()
        for x in nums:
            if freq[x]:
                freq[x] -= 1
                if end[x - 1] != 0:
                    end[x - 1] -= 1
                    end[x] += 1
                else:
                    if freq[x + 1] > 0 and freq[x + 2] > 0:
                        freq[x + 1] -= 1
                        freq[x + 2] -= 1
                        end[x + 2] += 1
                    else:
                        return False
        return True
