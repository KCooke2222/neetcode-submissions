class PrefixNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.tree = PrefixNode()
        
    def insert(self, word: str) -> None:
        curNode = self.tree
        i = 0
        while i < len(word) and word[i] in curNode.children:
            curNode = curNode.children[word[i]]
            i += 1

        while i < len(word):
            curNode.children[word[i]] = PrefixNode()
            curNode = curNode.children[word[i]]
            i += 1

        curNode.isEnd = True


    def search(self, word: str) -> bool:
        curNode = self.tree
        i = 0
        while i < len(word) and word[i] in curNode.children:
            curNode = curNode.children[word[i]]
            i += 1

        if i < len(word) or curNode.isEnd == False:
            return False
        else:
            return True


    def startsWith(self, prefix: str) -> bool:
        curNode = self.tree
        i = 0
        while i < len(prefix) and prefix[i] in curNode.children:
            curNode = curNode.children[prefix[i]]
            i += 1

        if i < len(prefix):
            return False
        else:
            return True
        
        