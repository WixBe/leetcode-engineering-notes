class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        left = k%sum(chalk)
        if left == 0:
            return 0 
        i=0
        while(left >= chalk[i]):
            left -= chalk[i]
            i = i+1 if i<len(chalk) else 0
        return i%len(chalk)