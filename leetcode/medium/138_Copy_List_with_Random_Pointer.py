"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap={None:None}
        ptr=head
        while ptr:
            copy=Node(ptr.val)
            hmap[ptr]=copy
            ptr=ptr.next
        ptr=head
        while ptr:
            copy=hmap[ptr]
            copy.next=hmap[ptr.next]
            copy.random=hmap[ptr.random]
            ptr=ptr.next
        return hmap[head]
