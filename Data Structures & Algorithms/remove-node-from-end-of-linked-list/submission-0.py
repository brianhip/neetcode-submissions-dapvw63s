# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        index = 0
        while fast and index < n:
            fast = fast.next
            index += 1
        
        if not fast:
            new_head = head.next
            head.next = None
            return new_head

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head