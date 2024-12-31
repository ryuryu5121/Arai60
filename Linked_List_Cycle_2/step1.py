def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    visited_nodes = set()
    while head:
        if head in visited_nodes:
            return head
        
        visited_nodes.add(head)
        head = head.next
    return None