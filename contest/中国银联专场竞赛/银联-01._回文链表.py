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
            

'''
不转化为数组。再克隆一个逆序的链表，进行对比。

145 / 145 个通过测试用例
状态：通过
执行用时: 4396 ms
内存消耗: 47.6 MB
'''
# 1 2 3 6 7 7 6 2 1
# 1 2 6 7 7 6 3 2 1
# n = 9, k = 2, n - 2 * k - 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # another, to store a reversed linked list of the origin
        node, n, another = head, 0, None
        while node:
            n += 1
            node1 = ListNode(node.val)
            node1.next = another
            another = node1
            # move to next one
            node = node.next
        
        def check(ptr1, ptr2, step):
            while step and ptr1 and ptr2:
                if ptr1.val != ptr2.val:
                    return False
                ptr1 = ptr1.next
                ptr2 = ptr2.next
                step -= 1
            return True
        
        n1, n2 = head, another
        k = 0
        while n1 and n2:
            if n1.val != n2.val:
                return check(n1.next, n2, n - k * 2 - 1) or check(n1, n2.next, n - k * 2 - 1)
            k += 1
            n1 = n1.next
            n2 = n2.next
            
        return True
            


