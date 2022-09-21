# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        while curr and curr.val == val:
            curr = curr.next
        
        head = curr
        lastGoodElement = head
        while curr:
            if curr.val == val:
                lastGoodElement.next = curr.next
            else:
                lastGoodElement = curr
            curr = curr.next
        return head