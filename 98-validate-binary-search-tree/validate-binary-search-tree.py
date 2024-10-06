# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tmp = []
        self.ans = True
        def dfs(node):
            if not node:
                return True
            dfs(node.left)
            if tmp and tmp[-1] >= node.val:
                self.ans = False
            tmp.append(node.val)
            dfs(node.right)
        dfs(root)
        print(tmp)
        return self.ans
        
            
                    