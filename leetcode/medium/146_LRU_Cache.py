#doubly linked list is used
class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.hmap={}#hash map for key to node mapping
        self.left=self.right=Node(0,0)#left pointer=LRU, right pointer=Most recent
        self.left.next=self.right
        self.right.prev=self.left
    #utility function to insert a node
    def add(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    #utility function to remove a node
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.hmap:
            self.remove(self.hmap[key])
            self.add(self.hmap[key])
            return self.hmap[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
        self.hmap[key]=Node(key,value)
        self.add(self.hmap[key])

        if len(self.hmap)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.hmap[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)