# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' Once again its the same way mate,
            1) Create a dummynode point it towards head.
            2) Traverse using fastpointer and slowpointer logic.
            3) Find middlenode.
            4) Delete it by adjusting the pointers and then done TA DA!
        '''

        # Handling edgecases
        if head is None or head.next is None:
            return None
        

        dummy = ListNode(0)
        dummy.next = head
        removalpointer = dummy
        fastpointer = slowpointer = head
        while fastpointer and fastpointer.next:
            slowpointer = slowpointer.next
            removalpointer = removalpointer.next
            fastpointer = fastpointer.next.next
        removalpointer.next = slowpointer.next
        return dummy.next
        