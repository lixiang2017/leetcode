# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def helper(a, b):
            if a is None and b is None:
                return True
            elif (a is None and b is not None) or (a is not None and b is None):
                return False
            else:
                return (a.val == b.val) and helper(a.left, b.left) and helper(a.right, b.right)

        return helper(p, q)


def test1():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    return Solution().isSameTree(p, q)


def test2():
    p = TreeNode(1)
    p.left = TreeNode(2)

    q = TreeNode(1)
    q.right = TreeNode(2)

    return Solution().isSameTree(p, q)


def test3():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)

    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)

    return Solution().isSameTree(p, q)


if __name__ == "__main__":
    assert test1()
    assert not test2()
    assert not test3()

