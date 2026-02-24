class Solution:    
    def lengthOfLongestSubstring(self, s: str) -> int:
        charin = {}
        maxln = 0
        left = 0

        for right, char in enumerate(s):
            if char in charin:
                left=max(left, charin[char]+1)
            charin[char] = right
            maxln = max(maxln, right-left+1)
        return maxln