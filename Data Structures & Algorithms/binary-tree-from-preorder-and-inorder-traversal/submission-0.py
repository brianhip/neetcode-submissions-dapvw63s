# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Iterate preorder and build left branch until reach smallest value in inorder
        # Use the inorder to know when to stop then keep using the preorder but update the inorder index to match pre
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) # preorder always has the root of current tree ( sub tree )
        mid = inorder.index(preorder[0]) # Inorder will have all the elements that should be left of current node so if find index we can get all elements to the left
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid]) # Slice all element to the left
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) # Slice all elements to the right and pass as arguments
        return root
        
