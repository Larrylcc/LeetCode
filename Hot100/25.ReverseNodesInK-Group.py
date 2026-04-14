# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev_group_tail = dummy
        group_head = head
        group_tail = dummy
        while True:
            for _ in range(k):
                if group_tail.next is None:
                    return dummy.next
                group_tail = group_tail.next
            next_group_head = group_tail.next
            group_tail.next = None
            new_head, new_tail = self.reverse(group_head)
            prev_group_tail = new_tail
            group_head = next_group_head
            group_tail = new_tail
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
