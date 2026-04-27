# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1  :
            return head
        
        dummy = ListNode(0,head)
        prev_group_end = dummy
        cur = head

        while cur :
            fast = cur

            for i in range(k-1):
                fast = fast.next
                if fast is None:
                    prev_group_end.next = cur
                    return dummy.next
            
            next_point = fast.next
            fast.next = None
        
            def reverseList(head:Optional[ListNode]):
                if not head or not head.next:
                    new_last = head
                    return head
                new_head = reverseList(head.next)
                head.next.next = head
                head.next = None
                return new_head

            new_head = reverseList(cur)
            prev_group_end.next = new_head
            cur.next = next_point

            prev_group_end = cur
            cur = next_point
            
        return dummy.next
            

        

        