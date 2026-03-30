# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        start = dummy
        pre = head
        end = dummy
        while True:
            for _ in range(k):
                if end.next is None:
                    return dummy.next
                end = end.next
            nxt = end.next
            end.next = None
            new_head, new_tail = self.reverse(pre)
            start.next = new_head
            new_tail.next = nxt
            pre = nxt
            start = new_tail
            end = new_tail
        return dummy.next

    def reverse(self, head: ListNode):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre, head
