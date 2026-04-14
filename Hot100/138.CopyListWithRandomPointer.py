
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        cur=head
        mapping={}
        # first loop: create new nodes
        while cur:
            new_node=Node(cur.val)
            mapping[cur]=new_node
            cur=cur.next
        cur=head
        # second loop: link next and random
        while cur:
            mapping[cur].next=mapping.get(cur.next)
            mapping[cur].random=mapping.get(cur.random)
            cur=cur.next
        return mapping[head]
