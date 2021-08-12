'''
heap
Time: O(3N + klogN)
Space: O(3N)

执行用时：44 ms, 在所有 Python3 提交中击败了75.67% 的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了11.11%
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num -> cnt
        c = Counter(nums)
        # cnt -> num
        c2 = [(-v, k) for k, v in c.items()]
        heapify(c2)
        ans = []
        while k:
            ans.append(heappop(c2)[1])
            k -= 1
        return ans


'''
执行用时：44 ms, 在所有 Python3 提交中击败了75.67% 的用户
内存消耗：17.7 MB, 在所有 Python3 提交中击败了17.13% 的用户
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num -> cnt
        c = Counter(nums)
        # cnt -> num
        c2 = [(-v, k) for k, v in c.items()]
        return [num for _, num in sorted(c2)[:k]]
