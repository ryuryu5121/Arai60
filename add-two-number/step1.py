class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_node = ListNode(0)
        place = 0
        sum_val = 0

        while l1 and l2:
            sum_val += 10 ** place * (l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next
        
        while sum_val:
            result_node.next = ListNode(sum_val % 10)
            result_node = result_node.next
            sum_val = sum_val // 10
        
        return result_node