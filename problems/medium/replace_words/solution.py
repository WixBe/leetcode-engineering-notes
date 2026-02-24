class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        lst = sentence.split()
        res=[]
        for i in lst:
            a=""
            for j in range(len(i)):
                a+=i[j]
                if a in dictionary:
                    break
            res.append(a)
        return " ".join(res) 
