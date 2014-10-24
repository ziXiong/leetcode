# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        elif self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False

def main():
    treelist1 = []
    treeroot1 = TreeNode(0)
    treelist1.append(treeroot)
    for i in range(1,10):
        tree = TreeNode(i)
        treelist1.append(tree)
        if i % 2 == 0:
            treelist1[i/2 - 1].right = tree
        else:
            treelist1[i/2].left = tree
            treelist1[i/2].right = tree
    treelist2 = []
    treeroot2 = TreeNode(0)
    treelist2.append(treeroot)
    for i in range(1,10):
        tree = TreeNode(i)
        treelist2.append(tree)
        if i % 2 == 0:
            treelist2[i/2 - 1].right = tree
        else:
            treelist2[i/2].left = tree
            treelist2[i/2].right = tree
    print(Solution.isSameTree(treeroot1, treeroot2))
    print("here")

if '__name__' == '__main__':
    main()
