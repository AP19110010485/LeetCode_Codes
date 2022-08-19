class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = len(arr)
        li = list(count.items())
        li.sort(key=lambda x: x[1])
        ans = 0
        removed_n = 0
        while removed_n < n/2:
            temp = li.pop()
            ans += 1
            removed_n += temp[1]
        return ans