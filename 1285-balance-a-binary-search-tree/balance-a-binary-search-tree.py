# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        def ans(l, r):
            if l > r: return
            mid = (l + r) // 2
            root = TreeNode(arr[mid])
            root.left = ans(l, mid - 1)
            root.right = ans(mid + 1, r)
            return root
        inorder(root)
        return ans(0, len(arr) - 1)