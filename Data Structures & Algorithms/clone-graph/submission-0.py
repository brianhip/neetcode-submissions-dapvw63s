"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        copy = {}
        def explore(curr_n):
            if curr_n in copy:
                return copy[curr_n]
            copy[curr_n] = Node(curr_n.val)
            for neigh in curr_n.neighbors:
                copy[curr_n].neighbors.append(explore(neigh))
            return copy[curr_n] 
        return explore(node)
