# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dhead = ListNode()
        cur = dhead

        carry=0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            t = val1 + val2 + carry
            carry = t//10

            cur.next = ListNode(t%10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dhead.next