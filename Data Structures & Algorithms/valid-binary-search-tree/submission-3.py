# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower_boundary: int = float("-inf"), upper_boundary: int = float("inf")) -> bool:
        if not root:
            return True
        if root.val <= lower_boundary or upper_boundary <= root.val:
            return False
        return self.isValidBST(root.left, lower_boundary, root.val) and self.isValidBST(root.right, root.val, upper_boundary)

    '''
        Idea: 
            We wqnt to make sure that at every point our recursive call knows of the boundaries imposed by their parents
            The children is not allowed to be outside those limit.
            If it happens that the children is outsite the limits we've found a possible break of the BST
    '''
        
        
