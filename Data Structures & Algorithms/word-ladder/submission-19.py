class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # O(n^2 * m)
        # O(n^2)
        # if endword dne return 0
        # adj list based on character transformation per word
            # cat: *at, c*t, ca*
            # these map to words that match the pattern
        # bfs over the adj list 
            # track visit set to avoid retraversing
            # go level by level using inner for loop
        # return level if endword found else 0

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        q = deque([beginWord])
        visit = set([beginWord])
        dist = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return dist
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nextWord in adj[pattern]:
                        if nextWord not in visit: 
                            q.append(nextWord)
                        visit.add(nextWord)

            dist += 1

        return 0

        
            
