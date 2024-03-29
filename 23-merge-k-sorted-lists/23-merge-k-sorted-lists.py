# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current_head_values = []
        while any(lists):
            for index, LL in enumerate(lists):
                if LL:
                    heapq.heappush(current_head_values, LL.val)
                    lists[index] = lists[index].next
        sentinel = ListNode(0)
        curr = sentinel
        for _ in range(len(current_head_values)):
            curr.next = ListNode(heapq.heappop(current_head_values))
            curr = curr.next
        return sentinel.next