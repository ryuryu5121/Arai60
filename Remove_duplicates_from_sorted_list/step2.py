#参考になったこと
#変数を定義することで逆に短期的記憶に影響が出て読みにくくなることもある



#参考になったコード
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = node = head

        while node and node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return result