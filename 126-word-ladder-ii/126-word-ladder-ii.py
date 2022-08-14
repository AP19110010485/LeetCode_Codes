class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        if endWord not in wordList: return []
        wordList = list(set(wordList))
        G = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                v = word[:i]+"*"+word[i+1:]
                G[v].add(word)
                G[word].add(v)
        #using BFS to construct predecessor array
        que = deque([(beginWord,0)])
        pred = defaultdict(list)
        visited = set()
        dist = defaultdict(lambda:float('inf'))
        while que:
            v, d = que.popleft()
            if v == endWord: break
            if v in visited: continue
            visited.add(v)
            for w in G[v]:
                if w not in visited:
                    if dist[w] == float('inf'):
                        dist[w] = d + 1
                        que.append((w,d+1))
                    if dist[w] == d+1:
                        pred[w].append(v)
        #enumerating all the shortest paths using backtracking
        res = []
        def dfs(v, path, goal):
            path.append(v)
            if v == goal:
                res.append(list(reversed(path))[::2])
            for w in pred[v]:
                dfs(w, path, goal)
            path.pop()
        dfs(endWord, [], beginWord)
        return res