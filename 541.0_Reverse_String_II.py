'''
 for every 2k characters # EVERY!!!
Success
Details 
Runtime: 16 ms, faster than 88.40% of Python online submissions for Reverse String II.
Memory Usage: 12.2 MB, less than 11.11% of Python online submissions for Reverse String II.
'''


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        res = ''  # str for '', list for []. not list!
        i = 0
        l = len(s)
        while True:
            if l <= k:
                res += s[i: i + l][::-1]
                break
            elif l <= 2 * k:
                res += s[i: i + k][::-1] + s[i + k: i + l]
                break
            else:
                res += s[i: i + k][::-1] + s[i + k: i + 2 * k]
                i += 2 * k
                l -= 2 * k

        return res


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
