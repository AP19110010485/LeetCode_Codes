class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n=len(s3)
        a,b=len(s1),len(s2)
        if (a+b)!=n:
            return False
        @cache
        def rec(i,j,k):
            if i==a and j==b and k==n:
                return True
            b1,b2=False, False
            
            if i<a and s1[i]==s3[k]:
                b1=rec(i+1,j,k+1)
                if b1: return True
            if j<b and s2[j]==s3[k]:
                b2=rec(i,j+1,k+1)
            return b1 or b2
        
        return rec(0,0,0)
        