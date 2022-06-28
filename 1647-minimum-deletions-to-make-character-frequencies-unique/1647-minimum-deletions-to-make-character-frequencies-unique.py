class Solution:
    def minDeletions(self, s: str) -> int:
        deletions=0
        char_counts=collections.Counter(s)
        lst=set()
        for val in char_counts.values():
            if val not in lst:
                lst.add(val)
            else:
                while val in lst and val>0:
                    val-=1
                    deletions+=1
                lst.add(val)
        return deletions
        