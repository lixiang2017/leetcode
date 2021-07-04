'''
Hash Table,T:O(2N),S:O(N)

执行用时：104 ms, 在所有 Python3 提交中击败了13.85% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了19.81% 的用户
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        freq = defaultdict(int)
        # find dup
        for num in nums:
            freq[num] += 1
            if freq[num] == 2:
                ans.append(num)
        # find missing
        for i in range(1, len(nums) + 1):
            if i not in freq:
                ans.append(i)
                break
        return ans