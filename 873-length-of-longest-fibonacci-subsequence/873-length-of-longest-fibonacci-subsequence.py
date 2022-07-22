class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s  = set(arr)
        last = arr[-1]
        B    = Counter()
        best = 0
        for i in reversed(range(len(arr))):
            a = arr[i]
            for b in arr[i+1:]:
                c = a+b
                if c in s:
                    B[a,b]  = 1 + B[b,c]
                    best    = max(best , B[a,b]+2)
                elif c>last:
                    break
        return best
        
        