# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        cur = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        if n == length:
            return head.next
        for i in range(0, length - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head


        