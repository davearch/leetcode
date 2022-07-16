# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        [1,2,4], [1,3,4] => [1,1,2,3,4,4]
        [], [] => []
        [], [0] => [0]
        [0], [0] => [0,0]
        """
        # maintain an unchanging reference to node ahead of the return node
        prehead = ListNode(-1)
        
        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        # at least one of list1 and list2 can still have nodes at this point
        prev.next = list1 or list2
        return prehead.next