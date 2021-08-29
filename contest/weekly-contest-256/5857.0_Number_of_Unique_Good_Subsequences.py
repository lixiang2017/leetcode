'''
1 <= binary.length <= 10^5

这种计数的，最后计数结果要 % MOD。
肯定不能把所有结果记录下来。这样太浪费时间，也太浪费空间了。
肯定是需要DP，定义好状态，找规律。

25 / 69 个通过测试用例
状态：超出时间限制
提交时间：5 小时前
最后执行的输入：
"111001101100000001001110110101110001100"
'''

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        seen = set()
        MOD = 10 ** 9 + 7
        for b in binary:
            # add first '1'
            if not seen and '1' == b:
                seen.add('1')
                continue
            if seen:
                new_added = set()
                for presub in seen:
                    # RuntimeError: Set changed size during iteration
                    if presub + b not in seen:
                        new_added.add(presub + b)
                        
                seen |= new_added

        if '0' in binary:
            seen.add('0')
        return len(seen) % MOD


