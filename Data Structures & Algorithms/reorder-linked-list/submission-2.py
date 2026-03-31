# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        self.head = head
        self.getSecondHead()
        self.reverseLinkedList()
        self.mergedLinkedList()

    def getSecondHead(self) -> None:
        slow = self.head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        self.head_two = slow
    
    def reverseLinkedList(self) -> None:
        prev_node = None
        curr_node = self.head_two
        while curr_node:
            temp_next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp_next
        self.head_two = prev_node
    
    def mergedLinkedList(self) -> None:
        if not self.head:
            return
        if not self.head_two:
            return
        curr1 = self.head
        curr2 = self.head_two
        while curr1 and curr2:
            temp_next1 = curr1.next
            temp_next2 = curr2.next
            curr1.next = curr2
            curr2.next = temp_next1
            curr1 = temp_next1
            curr2 = temp_next2
        
