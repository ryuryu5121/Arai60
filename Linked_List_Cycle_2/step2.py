
# LeetCodeの回答を基に修正, tortise and hare
class Solution(object):
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # あえて2行に分けることで可読性アップ
        slow = fast
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                break
        else: 
            return None  # if not (fast and fast.next): return None
        
        origin = head
        while origin != slow:
            origin = origin.next
            slow = slow.next
        return origin

# set()を使ったバージョンの修正
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    visited_nodes = set()
    node = head
    while node is not None:
        if node in visited_nodes:
            return node
        
        visited_nodes.add(node)
        node = node.next
    return None

