'''
31 / 39 个通过测试用例
状态：超出时间限制
提交时间：几秒前

Time: O(N^2)
Space: O(1)
'''

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                ans = max(ans, nums[i] ^ nums[j])
                
        return ans


'''
approach: Hash Set
Time: O((N + N) * logC) = O(NlogC), where N is the number of nums and C is the maximum of nums, so C == 31.
Space: O(N), for hash set.

执行用时：328 ms, 在所有 Python3 提交中击败了71.84% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了94.94% 的用户
'''
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        x = 0
        HIGH_BIT = 30
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            for num in nums:
                seen.add(num >> k)

            x_next = x * 2 + 1
            found = False
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break
            
            if found:
                x = x_next
            else:
                x = x_next - 1

        return x


'''
approach: Trie
Time: O(NlogC)
Space: O(NlogC)

执行用时：1504 ms, 在所有 Python3 提交中击败了14.55% 的用户
内存消耗：69 MB, 在所有 Python3 提交中击败了5.06% 的用户
'''
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self, nums):
        self.root = TrieNode()
        for n in nums:
            self.insert(n)
    
    def insert(self, n):
        cur = self.root
        for i in range(31, -1, -1):
            cur = cur.children[(n >> i) & 1]
    
    def searchMax(self, n):
        res, cur = 0, self.root
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            if bit ^ 1 in cur.children:  # 异或有交换律
                cur = cur.children[bit ^ 1]
                res += (1 << i)
            else:
                cur = cur.children[bit]
        return res

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        t = Trie(nums)
        return max([t.searchMax(n) for n in nums])



'''
approach: Trie
Time: O(NlogC)
Space: O(NlogC)

执行用时：1136 ms, 在所有 Python3 提交中击败了28.79% 的用户
内存消耗：35.6 MB, 在所有 Python3 提交中击败了68.35% 的用户
'''

class Trie:
    def __init__(self):
        # 0
        self.left = None
        # 1
        self.right = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        HIGH_BIT = 30

        def add(num: int):
            cur = root
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if 0 == bit:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right
        
        def check(num: int) -> int:
            cur = root
            x = 0
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if 0 == bit:
                    if cur.right:
                        cur = cur.right
                        x = x * 2 + 1
                    else:
                        cur = cur.left
                        x = x * 2
                else:
                    if cur.left:
                        cur = cur.left
                        x = x * 2 + 1
                    else:
                        cur = cur.right
                        x = x * 2
            return x
        
        n = len(nums)
        x = 0
        for i in range(1, n):
            add(nums[i - 1])
            x = max(x, check(nums[i]))
        return x







