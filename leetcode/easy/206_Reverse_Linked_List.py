# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative process
        prev,curr=None,head
        while curr:
            next_Curr=curr.next
            curr.next=prev
            prev=curr
            curr=next_Curr
        return prev

        #recursive process
        '''if not head:
            return None
        node=head
        if head.next:
            node=self.reverseList(head.next)
            print(node)
            head.next.next=head
        head.next=None
        return node'''
        