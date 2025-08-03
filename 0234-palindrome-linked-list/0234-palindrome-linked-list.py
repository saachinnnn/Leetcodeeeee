# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Handling Edgecases.
        if head is None:
            return False
        elif head.next is None:
            return True
        
        List : list = []

        curr = head
        while curr.next:
            List.append(curr.val)
            curr = curr.next
        List.append(curr.val)
        return List[::-1] == List[::]
