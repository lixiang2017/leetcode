Q: 给定一个棵完全二叉树，返回这棵树的节点个数，要求时间复杂度小于O(树的节点数)。
A: 右树最左节点层数==左树最左节点层数，左树是满二叉树，统计左树节点个数，递归右树。
右树最左节点层数!=左树最左节点层数，右树是满二叉树，统计右树节点个数，递归左树。
时间复杂度：O(logN的平方)。空间复杂度：O(logN)。