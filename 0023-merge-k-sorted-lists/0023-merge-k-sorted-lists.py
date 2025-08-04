class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []

        # Step 1: Flatten all node values into a single list
        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next

        # Step 2: Sort the values
        vals.sort()

        # Step 3: Build new sorted linked list
        dummy = ListNode(-1)
        tail = dummy
        for val in vals:
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next
