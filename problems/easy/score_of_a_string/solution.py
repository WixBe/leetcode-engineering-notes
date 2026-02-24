class Solution:
    def scoreOfString(self, s: str) -> int:
        score=0
        i = 0
        while(i+1<len(s)):
            score += abs(ord(s[i])-ord(s[i+1]))
            i+=1
        return score