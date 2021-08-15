'''
https://leetcode-cn.com/problems/TOVGD1/

执行用时：356 ms, 在所有 Python3 提交中击败了66.67% 的用户
内存消耗：11.2 MB, 在所有 Python3 提交中击败了27.78% 的用户
'''

n = int(input())

B = [-1] * n
A = list(map(int, input().split()))

m = int(input())
for _ in range(m):
    s = list(map(int, input().split()))
    if s[0] == 1:
        _, k, x, y = s
        B[y - 1: y - 1 + k] = A[x - 1: x - 1 + k]
    else: # == 2
        i = s[1] - 1
        print(B[i])



'''
输入：
5
1 2 3 4 5 
5
2 1
2 5
1 2 3 4
2 3
2 5
输出：
     -1
     -1
     -1
     4

输入：
5
1 2 3 4 5 
9
1 2 3 4
2 3
2 5
1 2 2 3
2 1
2 2
2 3
2 4
2 5
输出：
     -1
     4
     -1
     -1
     2
     3
     4
'''

