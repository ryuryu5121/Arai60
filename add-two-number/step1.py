class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_node = ListNode()
        place = 0
        sum = 0

        while l1 and l2:
            sum += 10 ** place * (l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next
        
        while sum:
            result_node.val = sum % 10
            result_node = result_node.next
            sum = sum / 10
        
        return result_node



