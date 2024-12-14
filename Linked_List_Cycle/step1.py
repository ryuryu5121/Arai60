class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        fast = head
        slow = head

        while(fast != None):
            if fast.next != None:
                fast = fast.next.next
            else:
                return False
            
            slow = slow.next

            if fast == slow:
                return True
        return False