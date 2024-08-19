# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        ans = []
        def backtrack(node, total, cur):
            if not node: return
            if not node.left and not node.right:
                if total + node.val == target:
                    ans.append(cur.copy() + [node.val])
                return
            cur.append(node.val)
            backtrack(node.left, total + node.val, cur)
            backtrack(node.right, total + node.val, cur)
            cur.pop()
        backtrack(root, 0, [])
        return ans