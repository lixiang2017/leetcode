'''
Simulation
先找环，再找循环节

看到题目，想到了无限循环小数中的循环节定义。
5.432768768768.... 循环节在'768'
7 -> 6 -> 8 -> 7 -> 6 -> 8 ...
题目中给的用例[-1,2]便是这样
0 -> 1 -> 1 -> 1 -> 1 -> 1 ...
类似这样的例子还有[-1,-1,3]，
1 -> 0 -> 2 -> 2 -> 2 -> 2 ...
[-1,-1,-1,4]
2 -> 1 -> 0 -> 3 -> 3 -> 3 ...

思考：人是怎么找循环节呢？
于是，暴力模拟人类寻找循环节的过程。
1、从每一位开始寻找，每一位的寻找过程跟其他位的寻找过程是相互独立的；
2、用seen记录经历过的索引。这个过程类似链表找环。同时想到或许可以用快慢指针方法；
3、最后看到的next_idx一定是在循环节中。重新用个new_seen记录这个过程，也就是去掉seen中非循环的数字；
4、要保证全正或者全负，也就是总是按照一个方向。可以用sign记录。
5、期间，如果找到，可以直接提前return true退出。


执行用时：268 ms, 在所有 Python3 提交中击败了46.09%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了13.67%的用户
'''
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        for i in range(N):
            seen = {i}
            next_idx = (i + nums[i]) % N
            while next_idx not in seen:
                seen.add(next_idx)
                next_idx = (next_idx + nums[next_idx]) % N
            # new
            new_seen = set()
            sign = 0
            while next_idx not in new_seen:
                new_seen.add(next_idx)
                if nums[next_idx] > 0:
                    sign += 1
                else:
                    sign -= 1
                next_idx = (next_idx + nums[next_idx]) % N            
            if len(new_seen) > 1 and abs(sign) == len(new_seen):
                return True
        
        return False
    


