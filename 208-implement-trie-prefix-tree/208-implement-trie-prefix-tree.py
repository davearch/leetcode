class Node:
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.isEnd = False
    
    def containsKey(self, ch: str) -> bool:
        return self.links[ord(ch) - ord('a')] != None
    
    def getKey(self, ch: str) -> 'Node':
        return self.links[ord(ch) - ord('a')]
    
    def setKey(self, ch: str, node: 'Node') -> None:
        self.links[ord(ch) - ord('a')] = node
    
    def setEnd(self):
        self.isEnd = True

    def isEndFunc(self):
        return self.isEnd

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            curr = word[i]
            if not node.containsKey(curr):
                node.setKey(curr, Node())
            node = node.getKey(curr)
        node.setEnd()

    def searchPrefix(self, word: str) -> 'Node':
        node = self.root
        for i in range(len(word)):
            curr = word[i]
            if not node.containsKey(curr):
                return None
            else:
                node = node.getKey(curr)
        return node
    
    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEndFunc()
        
    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)