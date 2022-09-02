class TrieNode:
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.isEnd = False
    
    def containsKey(self, ch: str) -> bool:
        return self.links[ord(ch) - ord('a')] != None
    
    def get(self, ch: str) -> 'TrieNode':
        return self.links[ord(ch) - ord('a')]
    
    def put(self, ch: str, node: 'TrieNode') -> None:
        self.links[ord(ch) - ord('a')] = node
    
    def setEnd(self) -> None:
        self.isEnd = True
    
    def isEndFunc(self) -> bool:
        return self.isEnd
    
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            currentChar = word[i]
            if not node.containsKey(currentChar):
                node.put(currentChar, TrieNode())
            node = node.get(currentChar)
        node.setEnd()
        
    def searchPrefix(self, word: str) -> TrieNode:
        node = self.root
        for i in range(len(word)):
            curLetter = word[i]
            if node.containsKey(curLetter):
                node = node.get(curLetter)
            else:
                return None
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