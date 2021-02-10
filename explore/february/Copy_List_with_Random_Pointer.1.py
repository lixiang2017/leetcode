'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: O(N)

ref:
https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/ha-xi-biao-dui-ying-xin-jiu-node-by-huan-2lin/

You are here!
Your runtime beats 99.05 % of python submissions.
You are here!
Your memory usage beats 89.56 % of python submissions.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return None
        copiedHead = Node(head.val)
        copiedNode = copiedHead
        old2new = {head: copiedHead}
        head_bak, copiedHead_bak = head, copiedHead
        
        while head.next:
            nextOld = head.next
            newNode = Node(nextOld.val)
            copiedNode.next = newNode
            old2new[nextOld] = newNode
            copiedNode = copiedNode.next
            head = head.next
            
        # for random
        while head_bak:
            if head_bak.random:
                copiedHead_bak.random = old2new[head_bak.random]
            
            head_bak = head_bak.next
            copiedHead_bak = copiedHead_bak.next
        
        return copiedHead
    