'''
Hash Table,T:O(2N),S:O(2N)
执行用时：48 ms, 在所有 Python3 提交中击败了49.81% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了41.03% 的用户
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
    def copyRandomList(self, head: 'Node') -> 'Node':
        # node to node pair
        old2new = {}
        old_node = head
        dummy = new = Node(x=-1)
        while old_node:
            new.next = Node(x=old_node.val)
            new = new.next
            old2new[old_node] = new
            old_node = old_node.next

        # random
        old_node = head
        while old_node:
            old2new[old_node].random = old2new[old_node.random] if old_node.random else None
            old_node = old_node.next

        return dummy.next


'''
执行用时：36 ms, 在所有 Python3 提交中击败了94.12% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了5.03% 的用户
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
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)




'''
DFS
执行用时：24 ms, 在所有 Python3 提交中击败了99.95% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了13.34% 的用户
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
    def copyRandomList(self, head: 'Node') -> 'Node':
        def copyNode(node, memo):
            if not node: return None
            if node in memo: return memo[node]
            copy = Node(node.val)
            # old to new pair, hash table
            memo[node] = copy
            copy.next = copyNode(node.next, memo)
            copy.random = copyNode(node.random, memo)
            return copy
        
        return copyNode(head, {})


'''
Recursion
执行用时：28 ms, 在所有 Python3 提交中击败了99.63% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了13.34% 的用户
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
    
    OLD2NEW = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        copy = Node(head.val)
        self.OLD2NEW[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.OLD2NEW.get(head.random)
        return copy
