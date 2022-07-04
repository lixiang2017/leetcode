'''
#   Author  Problem Lang    Verdict Time    Memory  Sent    Judged       
162644607   Practice:
lixiang2022 1700A - 10  PyPy 3-64   Accepted    155 ms  2860 KB 2022-07-03 15:59:14 2022-07-03 15:59:14

二维矩阵，从左上角到右下角。计算最小花费
看似是 DP 问题，实际最优解始终是
从左上角到右上角，再到右下角的路径。

证明： 假设路径随意从左上角到右下角。路径中最小的一个单元，也即四个单元格[a b c d]
      a -- b 
      |    |
      |    |
      c -- d
a -> b -> d
a -> c -> d 
由于按顺序标号，c > b 恒成立。
所以，路径 a -> c -> d 花费总是高于 a -> b -> d。
所以，路径 a -> c -> d 总是可以被 a -> b -> d 替换，而优化。
最终，从左上角到右上角，再到右下角的路径 是最优解。
'''


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    cost = m * (m - 1) // 2 + m * (1 + n) * n // 2
    print(cost)
    

