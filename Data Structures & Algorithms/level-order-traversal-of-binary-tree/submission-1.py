# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output_list = []
        queue = deque([[root, 1]])
        while len(queue):
            next_node, level = queue.popleft()
            if next_node.left:
                queue.append([next_node.left, level + 1])
            if next_node.right:
                queue.append([next_node.right, level + 1])
            if len(output_list) > level - 1:
                output_list[level - 1].append(next_node.val)
            else:
                output_list.append([next_node.val])
        return output_list
