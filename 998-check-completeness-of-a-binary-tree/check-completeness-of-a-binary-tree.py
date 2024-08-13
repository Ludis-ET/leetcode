# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, 0, 0)]
        position = 1
        while queue:
            node, level, column = queue.pop(0)
            if position != 2 ** level + column:
                return False

            if node.left:
                queue.append((node.left, level + 1, column * 2))
            if node.right:
                queue.append((node.right, level + 1, column * 2 + 1))

            position += 1

        return True
            