# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key: int):
        cur = root
        to_del = None
        if root is None:
            return root
        if (root.val == key and
            root.left is None and
            root.right is None):
            return None
        while True:
            if cur is None:
                return root
            if cur.val == key:
                to_del = cur
                break
            elif cur.val < key:
                cur = cur.right
            elif cur.val > key:
                cur = cur.left
        if (to_del.left is None and
            to_del.right is None):
            to_del = None
        elif to_del.left is None:
            to_del.val = to_del.left.val
            to_del.right = to_del.left.right
            to_del.left = to_del.left.left
        elif to_del.right is None:
            to_del.val = to_del.right.val
            to_del.left = to_del.right.left
            to_del.right = to_del.right.right
        else:
            prev = to_del
            change_to = to_del.right
            count = 0
            while change_to.left:
                prev = change_to
                change_to = prev.left
                count += 1
            to_del.val = change_to.val
            if count == 0:
                prev.right = None
            else:
                prev.left = None
        return root
