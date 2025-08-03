# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ''' How to solve this problem....
            Steps...
            1) Traverse through the Linkedlist.
            2) While traversing using currentpointer, if currenpointer.val matches with the desired value then delete it by updating the pointers to which it is pointing to.
            3) Then do the same till the currentpointer reaches the Last of the linkedlist.
        Done.'''

        # Creating a dummy to avoid the first element deletion edge case.
        dummy = ListNode(0)
        dummy.next = head
        currentpointer = dummy

        while currentpointer.next is not None:
            nextpointer = currentpointer.next
            if nextpointer.val == val:
                currentpointer.next = nextpointer.next
            else:
                currentpointer = currentpointer.next
        return dummy.next