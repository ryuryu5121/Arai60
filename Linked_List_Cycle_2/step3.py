class Solution(object):
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = slow

        while slow is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next.next

            if fast == slow:
                break
        else:
            return None
        
        origin = head
        while origin != slow:
            origin = origin.next
            slow = slow.next
        return origin
    
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    visited_nodes = set()
    node = head

    while node is not None:
        if node in visited_nodes:
            return node
        
        visited_nodes.add(node)
        node = node.next
    return None