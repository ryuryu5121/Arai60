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


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None, head)
        node = dummy_head

        while node.next and node.next.next:
            current_node = node.next
            next_node = current_node.next
            if current_node.val != next_node.val:
                node = node.next
                continue
            
            while next_node and current_node.val == next_node.val:
                next_node = next_node.next
            node.next = next_node
        
        return dummy_head.next