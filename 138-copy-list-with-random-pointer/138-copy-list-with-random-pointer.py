"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        sentinel = point = Node(0)
        curr = head
        while curr:
            node = Node(curr.val)
            temp = curr.next
            curr.next = node
            node.next = temp
            node.random = curr.random
            curr = curr.next.next
        
        count = 0
        curr = head
        while curr:
            if count % 2 != 0:
                if curr.random:
                    curr.random = curr.random.next
            curr = curr.next
            count += 1
        
        curr = head
        count = 0
        while curr:
            if count % 2 != 0:
                point.next = curr
                point = point.next
            curr = curr.next
            count += 1
        return sentinel.next
            
            
            
            
            
            
            