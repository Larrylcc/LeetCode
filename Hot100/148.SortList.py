# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        left=self.sortList(head)
        right=self.sortList(mid)
        return self.merge(left, right)

    def merge(self, l1:ListNode, l2:ListNode):
        dummy=ListNode(0)
        cur=dummy
        while l1 and l2:
            #temp=min(l1, l2, key=lambda node:node.val)
            if l1.val>l2.val:
                temp=l2
                l2=l2.next
            else:
                temp=l1
                l1=l1.next
            cur.next=temp
            cur=cur.next
        cur.next=l1 if l1 else l2
        return dummy.next
