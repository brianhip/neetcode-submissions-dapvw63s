# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        head_two = self.getSecondHead(head)
        reversed_head_two = self.reverseLinkedList(head_two)
        self.mergedLinkedList(head, reversed_head_two)

    def getSecondHead(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev_node = None
        curr_node = head
        while curr_node:
            temp_next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp_next
        return prev_node
    
    def mergedLinkedList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            temp_next1 = curr1.next
            temp_next2 = curr2.next
            curr1.next = curr2
            curr2.next = temp_next1
            curr1 = temp_next1
            curr2 = temp_next2
        return list1
