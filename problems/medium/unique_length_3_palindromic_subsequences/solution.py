class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) < 3:
            return 0
        res = 0
        for ch in set(s):
            first = s.find(ch)
            last = s.rfind(ch)
            if first < last - 1:
                res += len(set(s[first+1:last]))
        return res