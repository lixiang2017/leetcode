'''
47 / 60 个通过测试用例
状态：解答错误
提交时间：8 分钟前
最后执行的输入：
[5,5,5,5,20,20,5,5,5,5]


疑问：找钱必须要按照顾客排队的顺序吗？
假设可以不按顺序，先5，再10，再20

他们也太傻了，不知道变通一下。
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = Counter(bills)
        if freq[5] < freq[10]:
            return False
        freq[5] -= freq[10]

        # 1 freq[20] 需要  # 1 freq[5] + 1 freq[10] 
        # 一个10元 的可以用 两个5元 的补上
        for i in range(freq[20] + 1):
            # 换i个10元的, if need <= have
            if i * 2 + freq[20] <= freq[5] and freq[20] - i <= freq[10]:
                return True

        return False




'''
执行用时：60 ms, 在所有 Python3 提交中击败了64.00% 的用户
内存消耗：18.7 MB, 在所有 Python3 提交中击败了46.97% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for b in bills:
            if 5 == b:
                five += 1
            elif 10 == b:
                if five > 0:
                    five -= 1
                else:
                    return False
                ten += 1
            else:
                # 尽量用10块的
                if ten > 0:
                    ten -= 1
                    if five > 0:
                        five -= 1
                    else:
                        return False 
                elif five >= 3:
                    five -= 3
                else:
                    return False 

        return True


'''
执行用时：56 ms, 在所有 Python3 提交中击败了80.34% 的用户
内存消耗：18.7 MB, 在所有 Python3 提交中击败了35.47% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for b in bills:
            if 5 == b:
                five += 1
            elif 10 == b:
                five -= 1
                ten += 1
            else:
                # 尽量用10块的
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0 or ten < 0:
                return False

        return True


        