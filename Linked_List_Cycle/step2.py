class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True
        
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
         seen = set()
         while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
         return False