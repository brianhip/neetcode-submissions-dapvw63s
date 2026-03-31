# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if curr.val == subRoot.val -> check if same subtree
        if not root:
            return False
        if root.val == subRoot.val:
            is_same = self.isSameTree(root, subRoot)
            if is_same:
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
    
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)