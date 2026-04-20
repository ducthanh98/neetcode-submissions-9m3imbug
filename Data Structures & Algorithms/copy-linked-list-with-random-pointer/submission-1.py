"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        clone = {}

        first = head
        while first is not None:
            clone[first] = Node(first.val)
            first = first.next

        first = head
        second = clone[head]

        while first is not None:
            if first.next is not None:
                second.next = clone[first.next]
            if first.random is not None:
                second.random = clone[first.random]
            first = first.next
            second = second.next

        return clone[head] or []


