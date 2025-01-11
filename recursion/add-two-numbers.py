# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # def to_int(node):
        #     num, place = 0, 1
        #     while node:
        #         num += node.val * place
        #         place *= 10
        #         node = node.next
        #     return num
        
        # def to_list(number):
        #     dummy = ListNode()
        #     current = dummy
        #     if number == 0:
        #         return ListNode(0)
        #     while number > 0:
        #         current.next = ListNode(number % 10)
        #         number //= 10
        #         current = current.next
        #     return dummy.next
            
        # num1 = to_int(l1)
        # num2 = to_int(l2)
        # total = num1 + num2
        # return to_list(total)
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 

            total = val1 + val2 + carry
            carry = total // 10
            val = total % 10
            node = ListNode(val)
            curr.next = node

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


