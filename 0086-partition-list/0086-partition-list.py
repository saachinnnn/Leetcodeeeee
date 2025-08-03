# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ''' How to solve this problem.....
            Steps..
            1) Create two pointers , one for lower elements and one for higher elements.
            2) Merge them both at the end.
            3) Tail pointer / dummy node logic.
        '''

        # Handling edge cases.
        if head is None:
            return None
        
        before_element = ListNode(0)
        After_element = ListNode(0)

        before = before_element
        After = After_element

        curr = head
        while curr is not None:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                After.next = curr
                After = After.next 
            curr = curr.next
        
        After.next = None
        before.next = After_element.next

        return before_element.next
