'''
Time: O(N)
Space: O(N)

执行结果：通过
显示详情
执行用时：52 ms, 在所有 Python 提交中击败了27.78%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了40.97%的用户
'''

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        # first ^ encoded[0] -> arr[1]
        # arr[1] ^ encode[1] -> arr[2]
        arr = [first]
        for en in encoded:
            arr.append(arr[-1] ^ en)
        return arr
