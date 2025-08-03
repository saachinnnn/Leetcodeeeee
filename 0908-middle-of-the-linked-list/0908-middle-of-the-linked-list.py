# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowptr = fastptr = head
        while(fastptr is not None and fastptr.next is not None):
            slowptr = slowptr.next
            fastptr = fastptr.next.next
        return slowptr