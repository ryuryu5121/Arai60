class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_node = head
        fast_node = head
        while slow_node:
            while fast_node.next and fast_node.val == fast_node.next.val:
                fast_node.next = fast_node.next.next
            slow_node.next = fast_node.next
            fast_node = fast_node.next
        return slow_node