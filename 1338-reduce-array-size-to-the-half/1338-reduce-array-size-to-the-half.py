class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr).most_common()[::-1]
        
        out = 0
        sm = 0
        while sm < len(arr)/2:
            sm += cnt.pop()[1]
            out += 1
        
        return out
        