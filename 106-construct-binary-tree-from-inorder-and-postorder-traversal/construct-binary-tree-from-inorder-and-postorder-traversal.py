# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if not arr:
                return
            root = TreeNode(postorder.pop())
            i = arr.index(root.val)
            root.right = dfs(arr[i + 1:])
            root.left = dfs(arr[:i])
            return root
        return dfs(inorder)