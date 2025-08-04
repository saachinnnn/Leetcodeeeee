# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Handling edge cases.
        if head is None:
            return None
        
        Hashmap : dict = {}

        curr = head
        while curr:
            if curr.val not in Hashmap:
                Hashmap[curr.val] = 1
            else:
                Hashmap[curr.val] += 1
            curr = curr.next
        
        dummy = ListNode(-1)
        tail = dummy
        ptr = head
        while ptr:
            if Hashmap[ptr.val] == 1:
                tail.next = ptr
                tail = tail.next 
            ptr = ptr.next

        tail.next = None
        return dummy.next