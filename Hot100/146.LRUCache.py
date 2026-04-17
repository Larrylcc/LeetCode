from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=ListNode()
        self.tail=ListNode()
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if self.cache.get(key):
            temp=self.cache.get(key)
            self.remove_node(temp)
            self.add_to_head(self.head, temp)
            return temp.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value=value
            temp=self.cache[key]
            self.remove_node(temp)
            self.add_to_head(self.head, temp)
        else:
            new=ListNode(key, value)
            self.cache[key]=new
            self.add_to_head(self.head, new)
            if len(self.cache)>self.capacity:
                oldest_node=self.tail.prev
                self.remove_node(self.tail.prev)
                self.cache.pop(oldest_node.key)

    def remove_node(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def add_to_head(self, head, node):
        nxt=head.next
        head.next=node
        nxt.prev=node
        node.prev=head
        node.next=nxt

class ListNode:
    def __init__(self, key=0, value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
