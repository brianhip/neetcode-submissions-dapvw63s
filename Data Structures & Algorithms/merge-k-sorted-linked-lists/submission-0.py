# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
            Understand:
                Input: list with heads of linked lists
                Output: merged linked list -> Merge all linked list to ll with smallest head value
                Come up with average test case
                    [[1, 4, 8], [2, 3, 7], [3, 4, 5]]
                    [1, 2, 3, 3, 4, 4, 5, 7, 8]
                Edge Cases
                Tradeoffs (memory, performance)
                    Run: O(n * k) where n is the total number of nodes accross lists and k is number of lists
                    Space: O(1) 
            Match:
                linked list merging problem
                potentially used a dummy head that points to -> smallest -> 2nd smallest -> ... -> largest node
            Plan:
                Brute force Run:O(n * k)  Space:O(1) 
                    Create a dummy node for head
                    Create a dummy node for tail equal to head and move as your adding more nodes to represent the last node
                    Iterate until list has no remaider nodes (list length is 0)
                        Compare current nodes to add from each list to each other and add smallest after current linked list tail
                            Update the added node head to be the next node after the added node
                            If new head is none then pop off the list 
                            else update list node to be next node
                    return dummy node next node
                Use a min heap Run:O(n * log k) Space: O(k)
                    Create a dummy node for head
                    Create a dummy node for tail equal to head and move as your adding more nodes to represent the last node
                    Iterate until head has no remaider nodes (heap length is 0)
                        Pop smallest list_head.val from the heap
                        update list head to be the next if none then don't add to heap else add next to heap
                    return dummy node next node
        '''

        '''
            Implement:
        '''
        if not lists:
            return
    
        min_heap = []
        heapq.heapify(min_heap)
        for head in lists:
            if head is not None:
                heapq.heappush(min_heap, NodeWrapper(head))

        dummy_head = ListNode()
        tail = dummy_head
        while min_heap:
            smallest_node = heapq.heappop(min_heap).node
            if smallest_node.next:
                next_smallest_node = smallest_node.next
                smallest_node.next = None
                heapq.heappush(min_heap, NodeWrapper(next_smallest_node))
            tail.next = smallest_node
            tail = tail.next
        return dummy_head.next
        '''
            Review:
            Evaluate:
        '''