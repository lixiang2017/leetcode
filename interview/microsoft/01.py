
'''
Phone Screen (PS)
Mar 24 2022

https://leetcode-cn.com/problems/create-binary-tree-from-descriptions/

matrix
m  n 

parent, child, is_left(1/0)
[50, 20,  1] 
   50
   /
 20

[20, 15, 1]
[20, 17, 0]
[50, 80, 0]
[80, 19, 1]


[[50, 20, 1],
[20, 15, 1],
[20, 17, 0],
[50, 80, 0],
[80, 19, 1]]
  

       50
     20   80
   15 17,19   
   
50,  20  15 17    80 19

pre traversal list: [50, 20, 15, 17, 80, 19]


# seen = set()  dict()
'''

from collections import defaultdict


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right

class Solution:

    def buildBinaryTree(self, matrix):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        # val -> node
        val2node = dict()
        # val2deg, in_degree
        val2deg = defaultdict(int)
        # all node set
        nodes = set()

        for i, row in enumerate(matrix):
            print('row: ', row)
            print('type: ', type(row))
            parent, child, is_left = row
            p, ch = None, None
            if parent not in val2node:
                p = Node(parent)
                val2node[parent] = p 
            else:
                p = val2node[parent]

            if child not in val2node:
                ch = Node(child)
                val2node[child] = ch 
            else:
                ch = val2node[child]
            if 1 == is_left:
                p.left = ch 
            else:
                p.right = ch 

            # in_degree
            nodes.add(parent)
            nodes.add(child)
            val2deg[child] += 1

        for x in nodes:
            if val2deg[x] == 0:
                return val2node[x]

        return None 


def preOrder(node):
    if node:
        yield node.val 
        yield from preOrder(node.left)
        yield from preOrder(node.right)

def main():
    matrix = [[50, 20, 1],
        [20, 15, 1],
        [20, 17, 0],
        [50, 80, 0],
        [80, 19, 1]]    

    so = Solution()
    root = so.buildBinaryTree(matrix)
    print('root val: ', root.val)

    # pre
    print('pre traversal list:', list(preOrder(root)))
    

main()


'''
➜  /tmp python3 01.py
row:  [50, 20, 1]
type:  <class 'list'>
row:  [20, 15, 1]
type:  <class 'list'>
row:  [20, 17, 0]
type:  <class 'list'>
row:  [50, 80, 0]
type:  <class 'list'>
row:  [80, 19, 1]
type:  <class 'list'>
root val:  50

pre traversal list: [50, 20, 15, 17, 80, 19]
'''







