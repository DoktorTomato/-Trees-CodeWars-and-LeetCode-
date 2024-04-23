# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'{self.val} l: {self.left} | r: {self.right}'

class Solution:
    def deleteNode(self, root, key: int):
        if root is None:
            return root
        if root.val == key:
            if (root.left is None and
                root.right is None):
                root = None
            elif root.left is None:
                root.val = root.right.val
                root.left = root.right.left
                root.right = root.right.right
            elif root.right is None:
                root.val = root.left.val
                root.right = root.left.right
                root.left = root.left.left
            else:
                prev = root
                change_to = root.right
                count = 0
                while change_to.left:
                    prev = change_to
                    change_to = change_to.left
                    count += 1
                root.val = change_to.val
                if count == 0:
                    prev.right = None
                    root.right = change_to.right
                else:
                    prev.left = None
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(50, TreeNode(30, None, TreeNode(40)), TreeNode(70, TreeNode(60),TreeNode(80)))
    sol.deleteNode(tree, 50)
    print(tree)
