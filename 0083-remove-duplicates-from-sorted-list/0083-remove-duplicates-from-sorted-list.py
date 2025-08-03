class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        seen = set()
        dummy = ListNode(-1)
        tail = dummy
        curr = head

        while curr:
            if curr.val not in seen:
                seen.add(curr.val)
                tail.next = curr
                tail = tail.next
            # If duplicate, skip it by not updating tail
            curr = curr.next

        # Terminate the list
        tail.next = None

        return dummy.next