# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal until output count is less than k
        # return that value
        count = 0
        smallest_val = 0
        def inorder_traversal(node: Optional[TreeNode]) -> int:
            nonlocal smallest_val
            nonlocal count
            if not node:
                return
            inorder_traversal(node.left)
            count += 1
            if count == k:
                smallest_val = node.val
            inorder_traversal(node.right)
            return
    
        inorder_traversal(root)

        return smallest_val