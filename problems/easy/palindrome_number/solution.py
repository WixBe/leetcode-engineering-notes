class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        t=0
        l=len(str(x))
        for i in range(l//2):
            t=t*10+x%10
            x//=10
        if x==t or (x//10==t and l%2==1):
            return True
        else:
            return False
