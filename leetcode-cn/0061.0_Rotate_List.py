'''
approach: One Pass
Time: O(N)
Space: O(N)

执行用时：32 ms, 在所有 Python 提交中击败22.48%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了70.64%的用户
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        N, nodes, tail = self.onePass(head)
        # N = self.__len__(head)
        # N, tail = self.getLengthandTail(head)    
        k %= N
        if 0 == k or 1 == N:
            return head

        step = N - k
        newhead = nodes[step - 1].next
        nodes[step - 1].next = None
        tail.next = head
        return newhead

    
    def __len__(self, node):
        # wrong! 
        []
        0
        '''
        ZeroDivisionError: integer division or modulo by zero
            k %= N
        Line 16 in rotateRight (Solution.py)
            ret = Solution().rotateRight(param_1, param_2)
        Line 81 in _driver (Solution.py)
            _driver()
        Line 91 in <module> (Solution.py)
        '''
        cnt = 0
        while node:
            cnt += 1
            node = node.next
        return cnt


    def getLengthandTail(self, node):
        cnt = 0
        while node and node.next:
            cnt += 1
            node = node.next
        return cnt + 1, node
    
    def onePass(self, node):
        '''
        :rtype: [length(int), nodes(list), tail(node)]
        '''
        cnt = 0
        nodes = [node]
        while node and node.next:
            cnt += 1
            node = node.next
            nodes.append(node)
        return [cnt + 1, nodes + [node],node]
            

