# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
         How to solve these types of questions....
         Steps
         1) Detect if there are any cycles in the first place.
         2) If no cycle then return -1, is yes then Make the fastptr to the start of the linkedlist.
         3) Iterate now at the same pace, the slow and the fast pointer will meet eventually at the start.
         4) Return that node.
         Done.'''

         # Check for edge cases.
        if (head is None or head.next is None):
            return None
        
        fastpointer = slowpointer = head
        Checkiftheymeet : bool = False
        while fastpointer and fastpointer.next:
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next.next
            if fastpointer == slowpointer:
                Checkiftheymeet = True
                break
        if Checkiftheymeet:
            fastpointer = head
            if slowpointer == fastpointer:
                return head
            while fastpointer != slowpointer:
                fastpointer = fastpointer.next
                slowpointer = slowpointer.next
                if fastpointer == slowpointer:
                    return fastpointer
        else:
            return None