class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_val(node):
            if node is not None:
                return node.val
            return 0
        
        node_l1 = l1 
        node_l2 = l2 
        carry = 0
        dummy_head = ListNode()
        node_sum = dummy_head

        while node_l1 or node_l2 or carry > 0:
            temp_sum = get_val(node_l1) + get_val(node_l2) + carry
            carry, digit = divmod(temp_sum, 10)
            node_sum.next = ListNode(digit)
            node_sum = node_sum.next

            if node_l1:
                node_l1 = node_l1.next
            if node_l2:
                node_l2 = node_l2.next
        
        return dummy_head.next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        result = dummy_node
        carry_digit = 0

        while l1 or l2:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0
            sum_digit = val_l1 + val_l2 + carry_digit
            result.val = sum_digit % 10
            carry_digit = sum_digit // 10

            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next 
            if l1 or l2:
                result.next = ListNode()
                result = result.next
        
        if carry_digit > 0:
            result.next = ListNode(carry_digit)
        
        return dummy_node