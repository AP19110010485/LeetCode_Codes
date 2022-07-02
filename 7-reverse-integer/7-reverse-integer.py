class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0    
        if x>=0:
            while x>0:
                rem=x%10
                reverse=reverse*10+rem
                x=x//10
        
        if x<0:
            x=x*-1
            while x>0:
                rem=x%10
                reverse=reverse*10+rem
                x=x//10
            reverse=reverse*-1
        
        return reverse if -(2**31) < reverse < (2**31 - 1) else 0
            
            
        