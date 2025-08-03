# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        elif head.next is None:
            return False
        else:
            fastptr = slowptr = head
            while fastptr.next and fastptr.next.next:
                fastptr = fastptr.next.next
                slowptr = slowptr.next
                if slowptr == fastptr:
                    return True
        return False