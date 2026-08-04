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
        pre_list_node = ListNode()
        curr_node = pre_list_node

        i = list1
        j = list2
        while i and j:
            if i.val <= j.val:
                curr_node.next = i
                i = i.next
            else:
                curr_node.next = j
                j = j.next
            curr_node = curr_node.next

        while i:
            curr_node.next = i
            i = i.next
            curr_node = curr_node.next
        while j:
            curr_node.next = j
            j = j.next
            curr_node = curr_node.next

        return pre_list_node.next