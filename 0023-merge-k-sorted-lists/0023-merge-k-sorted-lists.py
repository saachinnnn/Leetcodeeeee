class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ''' To solve these type of problems.....

        1) Simply get the values from the nodes and store it as a list.
        2) Sort it and the stich it as a list.
         Done.'''

        vals : list = []

        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next
        
        vals.sort()

        dummy = ListNode(-1)
        tail = dummy
        for val in vals:
            tail.next = ListNode(val)
            tail = tail.next
        return dummy.next