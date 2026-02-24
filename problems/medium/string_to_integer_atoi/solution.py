class Solution:
    def myAtoi(self, s: str) -> int:
        max_int = 2**31-1
        min_int = -2**31
        s=s.strip()
        i=0
        num = 0
        sign=1
        if s=="":
            return 0
        if s[i]=='-':
            sign = -1
            i+=1
        elif s[i]=='+':
            i+=1
        while i<len(s) and s[i] in "0123456789":
            num=num*10+int(s[i])
            i+=1
        num*=sign
        if num < min_int:
            return min_int
        elif num > max_int:
            return max_int
        else:
            return num