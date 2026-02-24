class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[]
        l = set(words[0])
        for i in l:
            t = words[0].count(i)
            for word in words[1:]:
                y=word.count(i)
                t=min(t,y)
                if not t:
                    break
            res+=[i]*t
        return res