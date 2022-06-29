class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n=sorted(people, key=lambda x:(-x[0],x[1]))
        for i in range(len(n)):
            h,k=n[i]
            if k<i:
                s=n.pop(i)
                n.insert(k,s)
        return n
        