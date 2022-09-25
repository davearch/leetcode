# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        curr = point = ListNode(0)
        while arr:
            val = arr.pop()
            node = ListNode(val)
            curr.next = node
            curr = curr.next
        return point.next