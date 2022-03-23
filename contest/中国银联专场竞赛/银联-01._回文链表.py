'''
https://leetcode-cn.com/contest/cnunionpay-2022spring/problems/D7rekZ/
标准答案应该是错了

[1,2,2,3,1]
[5,1,8,8,1,5]
[1,2,3,4]
[4,8,6,6,6,8,4,8]
[4,8,6,6,8,4,8]

后两个 case 应该为 True, 但是标准答案的预期答案为 False.
我下面的程序也通过了。
这说明标准程序错了。而且测试用例也不充分。

后来反馈给他们小助理，他们已经改了过来。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        
        def check(x, y):
            while x < y:
                if arr[x] == arr[y]:
                    x += 1
                    y -= 1
                else:
                    return False
            return True
        
        i, j = 0, n - 1
        while i < j:
            if arr[i] == arr[j]:
                i += 1
                j -= 1
            else:
                return check(i, j - 1) or check(i + 1, j)
            
        return True
            
