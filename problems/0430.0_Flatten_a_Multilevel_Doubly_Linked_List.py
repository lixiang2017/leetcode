'''
DFS
T: O(2N)
S: O(N)

Runtime: 32 ms, faster than 91.14% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
Memory Usage: 15.7 MB, less than 7.81% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        flat = []
        
        def dfs(node):
            if not node:
                return 
            flat.append(node.val)
            dfs(node.child)
            dfs(node.next)
        
        dfs(head)
        # The linked list [1,2,3,7,8,11,12,9,10,4,5,6] is not a valid doubly linked list.
        # dummy = node = Node()   # wrong! should not have dummy node
        if not flat:
            return None
        first = node = Node(flat[0])
        i, N = 1, len(flat)
        while i < N:
            cur = Node(val = flat[i])
            node.next = cur
            cur.prev = node
            i += 1
            node = node.next
        return first





'''
Iteration
T: O(N)
S: O(1)

Runtime: 36 ms, faster than 76.43% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
Memory Usage: 14.5 MB, less than 97.93% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:   
            return head
        p = head
        while p:
            # case 1: if no child, proceed
            if not p.child:
                p = p.next
                continue
            # case 2: got child, find the tail of the child and link it to p.next
            ch = p.child
            while ch.next:
                ch = ch.next
            # connect tail with p.next, if it is not null
            ch.next = p.next
            if p.next:
                p.next.prev = ch
            # connect p with p.child, and remove p.child
            p.next = p.child
            p.child.prev = p
            p.child = None
            
        return head


'''
Recursion
T: O(N)
S: O(N)

Runtime: 40 ms, faster than 51.23% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
Memory Usage: 14.9 MB, less than 46.01% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        while p:
            if p.child:
                # remember the right node
                right = p.next
        
                # process its child group
                p.next = self.flatten(p.child)
                p.next.prev = p
                p.child = None
                # find the tail of child group
                while p.next:
                    p = p.next
                # connect the tail with right node
                if right:
                    p.next = right
                    p.next.prev = p
            # go to right node
            p = p.next
        
        return head
        
