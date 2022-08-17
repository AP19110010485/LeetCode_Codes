class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        store=set()
        for w in words:
            res=""
            for i in w:
                res+=dic[i]
            store.add(res)
        return len(store)
        
        