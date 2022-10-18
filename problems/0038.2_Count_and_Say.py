'''
recursion

Runtime: 51 ms, faster than 89.76% of Python3 online submissions for Count and Say.
Memory Usage: 14.1 MB, less than 16.06% of Python3 online submissions for Count and Say.
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        seq = self.countAndSay(n - 1)
        ans = []
        pre, cnt = '', 0
        for ch in seq:
            if pre != ch:
                if pre != '':
                    ans.append(str(cnt))
                    ans.append(pre)
                pre = ch
                cnt = 1
            else:
                cnt += 1
        ans.append(str(cnt))
        ans.append(seq[-1])
        return ''.join(ans)


'''
iteration

Runtime: 78 ms, faster than 62.13% of Python3 online submissions for Count and Say.
Memory Usage: 14.2 MB, less than 7.99% of Python3 online submissions for Count and Say.
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        seq = '1'
        for _ in range(n - 1):
            next_seq = []
            pre, cnt = '', 0
            for ch in seq:
                if pre != ch:
                    if pre != '':
                        next_seq.append(str(cnt))
                        next_seq.append(pre)
                    pre = ch
                    cnt = 1
                else:
                    cnt += 1
            next_seq.append(str(cnt))
            next_seq.append(seq[-1])
            seq = ''.join(next_seq)
        return seq 

