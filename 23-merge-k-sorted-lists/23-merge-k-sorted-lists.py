# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Wrapper:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        if not lists:
            return
        minheap = []
        for l in lists:
            if l:
                heapq.heappush(minheap, Wrapper(l))
        head = point = ListNode()
        while minheap:
            curr = heapq.heappop(minheap).node
            if curr:
                point.next = curr
                point = curr
                if curr.next:
                    heapq.heappush(minheap, Wrapper(curr.next))
        return head.next
            