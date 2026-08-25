class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # O(n * m)
        # O(1)
        # using a trie where each edge is suffix and pre char, with count
        # start from back, for each
            # compare with prev trie for number matches, add to res
        # add cur to trie by mapping its suffix and prefix

        class TrieNode:
            def __init__(self):
                self.children = {}
                self.count = 1

        res = 0

        trie = TrieNode()

        words.reverse()
        for word in words:
            # detection
            cur = trie
            for i in range(len(word)):
                edge = (word[i], word[len(word) - i - 1])
                if edge in cur.children:
                    cur = cur.children[edge]
                    if i == len(word) - 1:
                        res += cur.count
                else:
                    break

            # building trie
            cur = trie
            for i in range(len(word)):
                edge = (word[i], word[len(word) - i - 1])
                if edge in cur.children:
                    cur = cur.children[edge]
                    cur.count += 1
                else:
                    cur.children[edge] = TrieNode()
                    cur = cur.children[edge]



        return res