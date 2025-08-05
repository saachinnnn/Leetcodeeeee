# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        How to solve this problem....
        Steps...
        1) First we have to create a leftpreptr at the node left of the node at "Left".
        2) Then reverse till right - left + 1 (for loop)
        3) Then stich it accordingly.
        '''

        # Handling Exceptions.
        if head is None:
            return None
        

        dummy = ListNode(-1)
        dummy.next = head
        leftpreptr = dummy
        count : int = 1
        while count < left :
            leftpreptr = leftpreptr.next
            count += 1
        leftnode = leftpreptr.next

        preptr = None
        curr = leftnode
        for _ in range(right - left + 1):
            nextnode = curr.next
            curr.next = preptr
            preptr = curr
            curr = nextnode
        leftpreptr.next = preptr
        leftnode.next = curr
        return dummy.next