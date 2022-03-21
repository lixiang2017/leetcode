'''
T: O(N + 26*log26 + 26)
S: O(26)

Runtime: 67 ms, faster than 34.85% of Python3 online submissions for Partition Labels.
Memory Usage: 13.9 MB, less than 78.97% of Python3 online submissions for Partition Labels.
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # merge intervals for every distinct letter
        intervals = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if not intervals[idx]:
                intervals[idx] = [i, i]
            else:
                intervals[idx][-1] = i 
                
        intervals.sort()
        # merge intervals
        ms = []
        for inter in intervals:
            if not inter:
                continue
            # start, end
            s, e = inter
            if not ms or ms[-1][-1] < s:
                ms.append(inter)
            else:
                ms[-1][-1] = max(ms[-1][-1], e)
                
        return [m[1] -m[0] + 1 for m in ms]
            

'''
T: O(2N)
S: O(26)

Runtime: 71 ms, faster than 27.97% of Python3 online submissions for Partition Labels.
Memory Usage: 13.9 MB, less than 36.30% of Python3 online submissions for Partition Labels.
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last position/index for every letter
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
        
        ans = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord('a')])
            # if current index can be a end, cut it 
            if i == end:
                ans.append(end - start + 1)
                # start from next position
                start = i + 1
        
        return ans 
        
'''
T: O(2N)
S: O(26)

Runtime: 66 ms, faster than 36.52% of Python3 online submissions for Partition Labels.
Memory Usage: 13.8 MB, less than 78.97% of Python3 online submissions for Partition Labels.
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last position/index for every letter
        last = {ch: i for i, ch in enumerate(s)}
        
        ans = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            # if current index can be a end, cut it 
            if i == end:
                ans.append(end - start + 1)
                # start from next position
                start = i + 1
        
        return ans 
        

