class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        words.append(pattern)
        for i, word in enumerate(words):
            d = dict()
            c = 0
            new = ""
            for char in word:
                if(char not in d):
                    d[char] =c
                    c += 1
                new += str(d[char])
            words[i] = [words[i], new]
        ans = []
        for word in words[:-1]:
            if(word[1] == words[-1][1]):
                ans.append(word[0])
        return ans
        
	