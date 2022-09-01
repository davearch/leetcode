from sortedcontainers import SortedDict


class Node:
    def __init__(self,val=None,prev=None,nxt=None):
        self.val=val
        self.prev=prev
        self.next=nxt
        
        

class MaxStack:
    def __init__(self):
        self.stack=SortedDict()
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def _addNode(self,x):
        currhead=self.head.next
        currhead.prev=x
        x.next=currhead
        x.prev=self.head
        self.head.next=x
        
    def _delNode(self,x):
        prev=x.prev
        nxt=x.next
        prev.next=nxt
        nxt.prev=prev
        

    def push(self, x: int) -> None:#O(1)
        newNode=Node(x)
        self._addNode(newNode)
        if x not in self.stack:
            self.stack[x]=[newNode]
        else:
            self.stack[x].append(newNode)
    

    def pop(self) -> int:#O(1)
        nodeToRemove=self.head.next
        val=nodeToRemove.val
        self._delNode(nodeToRemove)
        if len(self.stack[val])>1:
            self.stack[val].pop()
        else:
            del(self.stack[val])
        return val

    def top(self) -> int:#O(1)
        return self.head.next.val

    def peekMax(self) -> int:#O(log(n))
        x=self.stack.peekitem()[0]
        return x
        

    def popMax(self) -> int:#O(log(n))
        x=self.stack.peekitem()
        self._delNode(x[-1][-1])
        self.stack[x[0]].pop()
        if len(self.stack[x[0]])==0:
            del(self.stack[x[0]])
        return x[0]