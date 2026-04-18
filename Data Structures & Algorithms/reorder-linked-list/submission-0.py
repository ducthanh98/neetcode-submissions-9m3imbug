# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        second_head = mid.next
        mid.next = None

        def reverse(node: Optional[ListNode]):
            if not node or not node.next:
                return node

            new_head = reverse(node.next)
            node.next.next = node
            node.next = None
            return new_head
        
        second = reverse(second_head)

        first = head

        while(second):
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            second = tmp2
            first= tmp1

