# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        secondHead = head
        while head and head.next is not None and secondHead and secondHead.next is not None and secondHead.next.next is not None:
            if head.next == secondHead.next.next:
                return True
            head = head.next
            secondHead = secondHead.next.next

        return False