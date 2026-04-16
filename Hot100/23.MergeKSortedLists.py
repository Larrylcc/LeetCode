import heapq
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap=[]
        dummy=ListNode(0)
        head=dummy
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap,(node.val, i, node))
        while min_heap:
            val, i, smallest_node=heapq.heappop(min_heap)
            head.next=smallest_node
            head=head.next
            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, i, smallest_node.next))
        return dummy.next

