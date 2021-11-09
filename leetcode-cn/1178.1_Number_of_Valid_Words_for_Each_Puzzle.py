'''
approach: Subsets(Permutation) + States Compression(Bit Manipulation) + Hash Table

执行用时：864 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：32.5 MB, 在所有 Python 提交中击败了100.00%的用户
Time: O(M*50 + N*2^6*7) = O(M + N), where M is the number of words and N is the number of puzzles.
Space:O(M + N), where M is for the hash table of words frequency and N is for the result.

ref:
https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/solution/zhuang-tai-ya-suo-zi-ji-ti-jie-yi-dong-c-bdx8/
'''




import collections

class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        freq = collections.Counter()
        for word in words:
            mask = 0
            for letter in word:
                mask |= 1 << (ord(letter) - ord('a'))
            freq[mask] += 1
        
        valid = []
        for puzzle in puzzles:
            total = 0
            for perm in self.subsets(puzzle[1:]):
                mask = 1 << (ord(puzzle[0]) - ord('a'))
                for ch in perm:
                    mask |= 1 << (ord(ch) - ord('a'))
                total += freq[mask]
            valid.append(total)
        return valid

    def subsets(self, puzzle):
        perms = [""]
        for letter in puzzle:
            perms += [item + letter for item in perms]
        return perms


'''
bitmask
执行用时：632 ms, 在所有 Python3 提交中击败了58.46% 的用户
内存消耗：44 MB, 在所有 Python3 提交中击败了24.61% 的用户
通过测试用例：10 / 10
'''
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ws = defaultdict(int)
        for w in words:
            x = 0
            for ch in w:
                x |= (1 << (ord(ch) - ord('a')))
            ws[x] += 1

        ans = []
        for p in puzzles:
            cnt = 0
            # p[0]
            for L in range(len(p)):
                for com in combinations(p[1:], L):
                    b = 0
                    for ch in com:
                        b |= (1 << (ord(ch) - ord('a')))
                    b |= (1 << (ord(p[0]) - ord('a')))
                    cnt += ws[b]

            ans.append(cnt)    
        
        return ans 

