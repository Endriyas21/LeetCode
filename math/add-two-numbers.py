# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_int(node):
            num, place = 0, 1
            while node:
                num += node.val * place
                place *= 10
                node = node.next
            return num
        
        def to_list(number):
            dummy = ListNode()
            current = dummy
            if number == 0:
                return ListNode(0)
            while number > 0:
                current.next = ListNode(number % 10)
                number //= 10
                current = current.next
            return dummy.next
            
        num1 = to_int(l1)
        num2 = to_int(l2)
        total = num1 + num2
        return to_list(total)