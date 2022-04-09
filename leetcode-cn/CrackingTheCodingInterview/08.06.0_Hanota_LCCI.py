'''
leetcode/leetcode-cn/CrackingTheCodingInterview/pictures/Tower_of_Hanoi.png
这个图片里的递归树显示了如何一步一步操作，能完成A->C的转移。
从代码实现来看，也是二叉树的中序遍历。
A[n]  B[]  C[]
要点：
借助一个空盘子(or 非空盘子，但是下方都是更大的盘子)，将[规模为n的问题]转化为[规模为n-1的问题]。
办法：
- A除开最下面的一个，剩余的n-1 借助于C 转移到 B
- A最下面的最大的盘子 转移到 C
- 跟第一步一样，B中的 n-1个盘子 借助于A 转移到 C

recursion/DFS
T: O(2^N - 1)
S: O(N)

执行用时：40 ms, 在所有 Python3 提交中击败了62.83% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了25.22% 的用户
通过测试用例：14 / 14

算法复杂度：
时间：
1、粗略估计
每次规模减小1，就会有一个move变成两个move。=> 以2为底的等比数列

2、精确计算
n = 1, f[1] = 1
n > 1, f[n] = 2 * f[n - 1] + 1
==> 构造等比数列，f[n] + 1 = 2 * (f[n - 1] + 1)
==> f[n] + 1 = 2^(n-1) * (f[1] + 1) = 2^n
==> f[n] = 2^n - 1


空间：
递归使用的栈空间。每次递归，空间规模减小 1， 所以栈需要 N 的空间。
'''


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        def move(n, a, b, c):
            if n == 1:
                c.append(a.pop())
            else:
                move(n - 1, a, c, b)
                c.append(a.pop())
                move(n - 1, b, a, c)
        
        move(n, A, B, C)



'''
同时计算出有多少操作才能完成A->C, 也就是时间复杂度。

执行用时：48 ms, 在所有 Python3 提交中击败了18.44% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了79.35% 的用户
通过测试用例：14 / 14
'''
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        # return operation count
        def move(n, a, b, c) -> int:
            if n == 1:
                c.append(a.pop())
                return 1
            else:
                cnt = 0
                cnt += move(n - 1, a, c, b)
                c.append(a.pop())
                cnt += 1
                cnt += move(n - 1, b, a, c)
                return cnt 
        
        total_cnt = move(n, A, B, C)
        print(total_cnt)


'''
执行用时：36 ms, 在所有 Python3 提交中击败了83.78% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了79.35% 的用户
通过测试用例：14 / 14
'''
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        def move(n, a, b, c):
            if n > 1:
                move(n - 1, a, c, b)
            c.append(a.pop())
            if n > 1:
                move(n - 1, b, a, c)
        
        move(n, A, B, C)



