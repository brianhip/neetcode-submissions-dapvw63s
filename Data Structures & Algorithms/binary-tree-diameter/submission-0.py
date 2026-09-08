# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is the longest lenth of left + right
        longest_diameter = [0]
        def dfs_depth(node, diameter):
            if not node:
                return 0
            left_depth = dfs_depth(node.left, diameter)
            right_depth = dfs_depth(node.right, diameter)

            diameter[0] = max(diameter[0], left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        dfs_depth(root, longest_diameter)
        return longest_diameter[0]
