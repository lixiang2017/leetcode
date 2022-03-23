'''
既然两个区间有同样多的 x 和同样多的 y，两区间的长度肯定相等。
两区间不能完全重叠，所以 s1 != s2, t1 != t2.

有时候，这些题目更像是脑筋急转弯。brainteaser
假设最后满足题意的子串为 sub1 和 sub2, 同时 s1 < s2, 即 sub1开始端 在 sub2开始端 的左侧。
随便举一些case。
假设字符串是 1XXX...XXXX1。 其中X既可以是0，也可以是1. 
去掉两头的两个1 之后的中间部分 XXX...XXXX。
可以这样构造 sub1, 最左侧的1 + 中间部分 XXX...XXXX.
可以这样构造 sub2, 中间部分 XXX...XXXX + 最右侧的 1.
神奇地发现 sub1跟sub2竟然满足题意，那是因为中间部分是公共的，可以不用管有多少x,有多少y.

同理，0XXX...XXXX0，也是一样的构造 sub1 = 0XXX...XXXX 和 sub2 = XXX...XXXX0.
'11111000'  这种情况，只能用那片更长的1了，sub1 = 1111, sub2 = 1111
'0000011'   这种情况，只能用那片更长的0了，sub1 = 0000, sub2 = 0000

总结来看，就是找最远的两端一样的字符（要么全为0，要么全为1），然后错开一个位置就行。
其实就两种选择。
1、从尾端逆序找跟 s[0] 一样的字符；2、从起始端正序找跟 s[n-1] 一样的字符。
然后，这两种情况，取更长的就行。

复杂度
T: O(2N) = O(N)
S: O(1)
'''

from typing import List

class Solution:

    def findTwoLongestIntervals(self, s: str) -> List[int]:
        # return [start1, terminal1, start2, terminal2]
        s1 = t1 = s2 = t2 = None
        n = len(s)
        if n < 2:
            return []

        # s[0], check from the end of s, find letter which is same as s[0]
        j = n - 1
        while j > 0 and s[j] != s[0]:
            j -= 1
        s1, t1, s2, t2 = 0, j - 1, 1, j

        # s[n - 1], check from the beginning of s, find letter which is same as s[n - 1]
        i = 0
        while i < n and s[i] != s[n - 1]:
            i += 1
        # if longer than last one    0...j   i...n-1
        if n - 1 - i > j:
            s1, t1, s2, t2 = i, n - 2, i + 1, n - 1
        return [s1, t1, s2, t2]

def main():
    so = Solution()
    s = '11011'   # '1101'   '1011'
    assert(so.findTwoLongestIntervals(s) == [0, 3, 1, 4])

    s = '00011111000'
    assert(so.findTwoLongestIntervals(s) == [0, 9, 1, 10])

    s = '11100000111'
    assert(so.findTwoLongestIntervals(s) == [0, 9, 1, 10])

    s = '11111000'
    assert(so.findTwoLongestIntervals(s) == [0, 3, 1, 4])

    s = '0000011'
    assert(so.findTwoLongestIntervals(s) == [0, 3, 1, 4])

    s = '1100000'   # '0000' '0000'
    assert(so.findTwoLongestIntervals(s) == [2, 5, 3, 6])

    s = '101'   # '10'  '01'
    assert(so.findTwoLongestIntervals(s) == [0, 1, 1, 2])    

if __name__ == '__main__':
    main()

