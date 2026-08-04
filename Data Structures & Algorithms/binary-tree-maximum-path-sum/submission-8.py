# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            curr_path_sum = root.val + leftMax + rightMax
            max_path_sum[0] = max(max_path_sum[0], curr_path_sum)

            best_branch =  max(leftMax, rightMax)
            return root.val + best_branch

        dfs(root)
        return max_path_sum[0]