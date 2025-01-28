class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()

        forward = head.next
        later = head

        while forward is not None:
            if forward in visited:
                forward = forward.next
            elif forward not in visited:
                visited.add(forward)
                forward = forward.next
                later = later.next
        return forward

