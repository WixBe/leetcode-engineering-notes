class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        else:
            j=0
            for i in range(len(s)):
                if j<len(t) and t[j]==s[i]:
                    j+=1
            return len(t)-j