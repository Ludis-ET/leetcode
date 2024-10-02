# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre):
            if not pre:
                return       
            root = TreeNode(pre.popleft())
            left = deque()
            while pre and pre[0] < root.val:
                left.append(pre.popleft())
            root.left = dfs(left)
            root.right = dfs(pre)
            return root
        return dfs(deque(preorder))