# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new=ListNode()
        ptr=new
        c=0
        while l1 or l2 or c:
            value1=l1.val if l1 else 0
            value2=l2.val if l2 else 0

            total=value1+value2+c
            c=total//10
            total=total%10
            ptr.next=ListNode(total)
            ptr=ptr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
