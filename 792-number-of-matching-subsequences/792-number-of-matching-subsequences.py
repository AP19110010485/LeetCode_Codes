class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        for word in words:
            temp=s
            found = True
            for letter in word:
                ind = temp.find(letter)
                if ind != -1:
                    temp = temp[ind+1:]
                else:
                    found = False
                    break
                    
            if found:
                count +=1
        return count
        