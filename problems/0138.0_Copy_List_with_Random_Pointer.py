'''
hash table + iteration

T: O(N + N) = O(N)
S: O(N + N) = O(N)

Runtime: 32 ms, faster than 97.30% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 15 MB, less than 29.48% of Python3 online submissions for Copy List with Random Pointer.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new = dict()
        node = head
        # create node
        while node:
            old2new[node] = Node(node.val)
            node = node.next 
        
        # set pointer
        node = head
        while node:
            # set next pointer
            old_next = node.next
            if old_next:
                new_next = old2new[old_next]
                old2new[node].next = new_next
            # set random pointer
            old_random = node.random
            if old_random:
                new_random = old2new[old_random]
                old2new[node].random = new_random
            
            # move to next one
            node = node.next
        
        return old2new[head] if head else None
    

'''
Runtime: 89 ms, faster than 5.51% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 18.2 MB, less than 9.15% of Python3 online submissions for Copy List with Random Pointer.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return copy.deepcopy(head)
        


'''
hash table + recursion
T: O(N)
S: O(N)

Runtime: 78 ms, faster than 6.81% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 15.4 MB, less than 9.15% of Python3 online submissions for Copy List with Random Pointer.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new = dict()
        
        def dfs(node: Optional[Node]):
            if not node:
                return None
            if node in old2new:
                return old2new[node]
            
            new_node = Node(node.val)
            old2new[node] = new_node
            # do next pointer and random pointer in a recursion way
            new_node.next = dfs(node.next)
            new_node.random = dfs(node.random)
            return new_node
        
        return dfs(head)
    

'''
hash table + recursion
T: O(N)
S: O(N)

Runtime: 53 ms, faster than 49.58% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 15.5 MB, less than 9.15% of Python3 online submissions for Copy List with Random Pointer.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.old2new = dict()
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # consider head as a common node
        if not head:
            return None
        if head in self.old2new:
            return self.old2new[head]
        
        new_head = Node(head.val)
        # set memoization
        self.old2new[head] = new_head
        # set next pointer and random pointer in a recusion way
        new_head.next = self.copyRandomList(head.next)
        new_head.random = self.copyRandomList(head.random)
        return new_head
    





