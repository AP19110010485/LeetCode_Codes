class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        que = set([(startRow, startColumn)])
        cnts = {(startRow,startColumn):1}
        M = 10**9 + 7
        res = 0
        while que and maxMove:
            nxt_que = set()
            nxt_cnts = defaultdict(int)
            maxMove -= 1
            while que:
                i,j = que.pop()
                for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                    if 0<=i+di<m and 0<=j+dj<n:
                        nxt_cnts[(i+di,j+dj)] = (nxt_cnts[(i+di,j+dj)]+cnts[(i,j)])%M
                        if (i+di,j+dj) not in nxt_que:
                            nxt_que.add((i+di,j+dj))
                    else:
                        res = (res + cnts[(i,j)])%M
            que = nxt_que
            cnts = nxt_cnts
        return res
       