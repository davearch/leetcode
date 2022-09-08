# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        temp = head.next
        head.next = temp.next
        temp.next = head
        
        node = self.swapPairs(head.next)
        head.next = node
        return temp
        