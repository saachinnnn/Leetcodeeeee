# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' How to solve this problem....
            Steps:-
            1) Just use the dummy node method and keep a tailpointer and maintain a hashset LMFAO.
            2) DONE TA DA!
            '''

            # First the edge cases.
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            Hashset : set = set()
            dummy = ListNode(-1)
            tail = dummy
            tail.next = head
                
            curr = head
            while curr is not None:
                if curr.val in Hashset:
                    tail.next = curr.next
                else:
                    Hashset.add(curr.val)
                    tail.next = curr
                    tail = tail.next
                curr = curr.next
            return dummy.next