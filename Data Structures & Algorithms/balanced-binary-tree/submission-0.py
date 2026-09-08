# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def dfs(node):
            nonlocal is_balanced
            if not node or not is_balanced:
                return 0
            l_depth = dfs(node.left)
            r_depth = dfs(node.right)
            if abs(l_depth - r_depth) > 1:
                is_balanced = False
            return max(l_depth, r_depth) + 1
        dfs(root)
        return is_balanced