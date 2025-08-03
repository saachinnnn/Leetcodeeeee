# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
            Steps to solve such problems....
            1) Reverse the linkedlist first to find the nth node to delete.
            2) Create a dummy node pointing to the first node.
            3) Then delete the node using curr.next = curr.next.next type thing
            4) Finally reverse it back to retain the order of the LL.
            5) Return it.
        '''
        if head is None:
            return None
        elif head.next is None:
            return None if n == 1 else head

        # Reverse the Linkedlist.
        preptr = None
        ptr = head
        while ptr is not None:
            nextptr = ptr.next
            ptr.next = preptr
            preptr = ptr
            ptr = nextptr
        
        # Create a Dummy Node and delete the node which is desired according to the question.
        dummy = ListNode(0)
        dummy.next = preptr # preptr is the new head.
        curr = dummy
        for _ in range(n - 1):
            curr = curr.next
        
        curr.next = curr.next.next

        # Now the node is removed , now reverse everything back again.
        preptr = None
        ptr = dummy.next
        while ptr is not None:
            nextptr = ptr.next
            ptr.next = preptr
            preptr = ptr
            ptr = nextptr
        
        # Now again preptr becomes the new node.
        # Thus
        return preptr