# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        list_head = ListNode()
        list_tail = list_head
        while list1 and list2:
            # Add smallest
            if list1.val <= list2.val:
                list_tail.next = ListNode(list1.val)
                list_tail = list_tail.next
                list1 = list1.next
            else:
                list_tail.next = ListNode(list2.val)
                list_tail = list_tail.next
                list2 = list2.next
        while list1:
            list_tail.next = ListNode(list1.val)
            list_tail = list_tail.next
            list1 = list1.next
        while list2:
            list_tail.next = ListNode(list2.val)
            list_tail = list_tail.next
            list2 = list2.next
        return list_head.next