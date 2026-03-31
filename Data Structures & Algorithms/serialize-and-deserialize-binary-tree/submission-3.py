# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        '''
            if not root return "null"
            res = []
            BFS level traversal 
            create a queue with first node -> while queue is not empty -> pop next element in the queue -> append value of node to a result list -> add children to the queue
            join res values with commas
        '''
        if not root:
            return "null"
        output = []
        queue = deque([root])
        while queue:
            next_node = queue.popleft()
            if not next_node:
                output.append("null")
            else:
                output.append(str(next_node.val))
                queue.append(next_node.left)
                queue.append(next_node.right)
        return ",".join(output)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        '''
            split data
            if first value in data was a "null" -> return None
            create a root node
            Since we used BFS to serialize it, we should use it deserilize it
            use a queue to keep track of the next node we're going to connect to their children
            while the queue is not empty iterate the string using an index
                get next available node -> create the nodes for children -> connect current node to both children -> children to queue
            returnr root
        '''
        data_lst = data.split(",")
        if data_lst[0] == "null":
            return None
        root = TreeNode(int(data_lst[0]))
        queue = deque([root]) 
        index = 1
        while queue:
            next_node = queue.popleft()
            if data_lst[index] != "null":
                next_node.left = TreeNode(int(data_lst[index]))
                queue.append(next_node.left)
            index += 1
            if data_lst[index] != "null":
                next_node.right = TreeNode(int(data_lst[index]))
                queue.append(next_node.right)
            index += 1
        return root