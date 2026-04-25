# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        head = dummy
        print(len(lists))
        h = len(lists)

        while True:
            min_num = 9999999999
            min_idx = 0
            need_out = True
            for i in range(h):
                
                if lists[i] is not None:
                    need_out = False
                    if lists[i].val < min_num:
                        min_num = lists[i].val
                        min_idx = i
                    

            if need_out:
                return head.next
            else:
                dummy.next = lists[min_idx]
                lists[min_idx] = lists[min_idx].next
                dummy = dummy.next
