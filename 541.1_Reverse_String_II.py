'''
Success
Details 
Runtime: 20 ms, faster than 69.61% of Python online submissions for Reverse String II.
Memory Usage: 12.2 MB, less than 11.11% of Python online submissions for Reverse String II.
Next challenges:
'''


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a = list(s)
        for i in xrange(0, len(s), 2 * k):
            a[i: i + k] = reversed(a[i: i + k])

        return ''.join(a)


if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    assert Solution().reverseStr(s, k) == "bacdfeg"

    s = "krmyfshbspcgtesxnnljhfursyissjnsocgdhgfxubewllxzqhpasguvlrxtkgatzfybprfmmfithphckksnvjkcvnsqgsgosfxc"
    k = 20
    # my first try output
    # "jlnnxsetgcpsbhsfymrkhfursyissjnsocgdhgfxtxrlvugsaphqzxllwebukgatzfybprfmmfithphckksnvjkcvnsqgsgosfxc"
    assert Solution().reverseStr(s, k) == \
        "jlnnxsetgcpsbhsfymrkhfursyissjnsocgdhgfxtxrlvugsaphqzxllwebukgatzfybprfmmfithphccxfsogsgqsnvckjvnskk"
