# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        while pre.next and pre.next.next:
            cur = pre.next
            suf = cur.next
            nxt = suf.next
            pre.next, suf.next, cur.next = suf, cur, nxt
            pre = cur
        return dummy.next
