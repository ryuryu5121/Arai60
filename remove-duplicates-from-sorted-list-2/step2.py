class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        result = dummy
        node = head
        while node:
            if node.next and node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node.next = node.next.next
                node = node.next
                continue
            else:
                result.next = ListNode(node.val)
                result = result.next
                node = node.next
                continue
        return dummy.next