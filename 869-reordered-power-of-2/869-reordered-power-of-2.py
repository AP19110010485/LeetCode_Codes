class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_str = str(n)
        n_count = Counter(n_str)
        # Collect all powers of 2 that could be created by rearranging n
        # We keep going until n^2 because in some cases it could be larger than n (46 -> 64)
        at = 1
        pows = []
        while at <= n**2:
            pows.append(at)
            at = at * 2
        
        # Check if each power matches by counting the digits in each
        # Check length first because it is an O(1) operation
        for power in pows:
            if len(n_str) == len(str(power)):
                if Counter(str(power)) == n_count:
                    return True
        return False