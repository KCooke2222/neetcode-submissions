class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for word in words:
            trie.insert(word)

        
        path = []
        res = set()
        visit = set()

        def dfs(r, c, cur):
            char = board[r][c]
            if char not in cur.children:
                return

            path.append(char)
            visit.add((r, c))

            cur = cur.children[char]

            if cur.end:
                res.add("".join(path))

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if (nr, nc) in visit:
                    continue
                if not (0 <= nr < len(board) and 0 <= nc < len(board[0])):
                    continue
                
                dfs(nr, nc, cur)

            path.pop()
            visit.remove((r, c))

            
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, trie.root)

        return list(res)
