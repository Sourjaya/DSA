# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from os import preadv


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        #finding mid node
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        rev=None
        # reverse second half of linked list

        '''
            the rev will store the reversed linked list.
            if a linked list is given:
                1 -> 2 -> 3
                slow points to - 1
            for each iteration slow will be next of slow which is being achieved by the extra variable temp.
            temp=slow.next
            slow=temp
            This two lines does the above operation
            Now,
            slow.next=rev
            This line attaches the reversed linked list to the current node pointed by slow.
            rev=slow
            the attached linked list becomes the new reversed linked list
        '''
        while slow:
            temp=slow.next
            slow.next=rev
            rev=slow
            slow=temp
        # checking for palindrome
        left ,right=head,rev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True

