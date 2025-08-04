# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Handling exceptions.
        if l1 is None and l2 is None:
            return None
        elif l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l1 is None:
            return l1
        
        # Now for the Main Logic.

        dummy = ListNode(-1)
        tail = dummy
        carry : int = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total : int = val1 + val2 + carry
            carry = total // 10
            Newnode = ListNode(total % 10)

            tail.next = Newnode
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next