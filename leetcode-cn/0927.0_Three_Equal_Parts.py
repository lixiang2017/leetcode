'''
逆序模拟
T： O（N）
S： O（1）

执行用时：60 ms, 在所有 Python3 提交中击败了84.17% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了43.89% 的用户
通过测试用例：121 / 121
'''
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        cnt = Counter(arr)
        if cnt[1] == 0:
            if len(arr) < 3:
                return [-1, -1]
            else:
                return [0, 2]
        if cnt[1] % 3 != 0:
            return [-1, -1] 
        one = cnt[1] // 3
        n = len(arr)
        # the third part 
        third0 = third1 = 0
        i = n - 1
        while i >= 0 and arr[i] == 0:
            third0 += 1
            i -= 1
        while i >= 0 and third1 < one:
            if arr[i] == 1:
                third1 += 1
            i -= 1

        cand_j = i + 1  # rightmost candidate j
        # the second part 
        second0 = second1 = 0
        while i >= 0 and arr[i] == 0:
            second0 += 1
            i -= 1
        while i >= 0 and second1 < one:
            if arr[i] == 1:
                second1 += 1
            i -= 1 
        cand_i = i  # rightmost candidate i 
        # the first part
        first0 = 0
        while i >= 0 and arr[i] == 0:
            first0 += 1
            i -= 1

        #       first0            second0             third0 
        # 0.....000 cand_i | 1....1000 | cand_j 1....1000 n-1
        if second0 < third0 or first0 < third0:
            return [-1, -1] 
        one_len = n - third0 - cand_j
        f_one = arr[cand_i - first0 + 1 - one_len: cand_i - first0 + 1]
        s_one = arr[cand_j - second0 - one_len: cand_j - second0]
        t_one = arr[cand_j: n - third0]
        if f_one != t_one or s_one != t_one:
            return [-1, -1]
        i = cand_i - first0 + third0 
        j = cand_j - second0 + third0 
        return [i, j]
        
        




