# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        prehead -> linkedlist
            recursive function reversek takes previous node to be connected to this seciton
                base case if not node or not node.next return node

                move k numbers forward and cache node k + 1 as the successor 
                
                cache head as future_tail

                reversal of the linked list size k
                while curr_reversed < k and curr:
                    pre -> curr -> (none or node)
                    pre <- curr <- temp
                    __  <- prev <- curr
                    
                    temp = curr.next
                    curr.next= prev

                    prev = curr
                    curr = temp
                
                if successor:
                    future_tail.next = recursive_call(successor)

                return prev                
        """
        return self.reverseSectionK(head, k)

    def reverseSectionK(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not node or not node.next:
            return node
        # print("head", node.val)

        future_tail = node
        curr_tail = node
        i = 0
        while i < k - 1 and curr_tail and curr_tail.next:
            curr_tail = curr_tail.next
            i += 1
        # print("curr tail", curr_tail)
        # print("i", i, "k", k)
        if i < k - 1:
            return node
        successor = curr_tail.next if curr_tail else None
        # print("successor", successor)
        i = 0
        prev = None
        while i < k and node:
            temp = node.next
            node.next= prev

            prev = node
            node = temp
            i += 1

        if successor:
            future_tail.next = self.reverseSectionK(successor, k)
        
        return prev