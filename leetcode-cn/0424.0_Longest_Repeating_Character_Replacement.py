'''
approach: Two Pointers
Time: O(N)
Space: O(length(hashtable)) = O(sigma)

执行结果：通过
显示详情
执行用时：44 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了81.61%的用户
'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        size = len(s)
        i = j = 0
        # hashtable = [0 for _ in range(26)]
        hashtable = defaultdict(int)
        max_count = 0
        while i < size and j < size:
            hashtable[s[j]] += 1
            max_count = max(hashtable[s[j]], max_count)
            if (j - i + 1 - max_count) > k:
                hashtable[s[i]] -= 1
                i += 1

            j += 1

        return j - i
        