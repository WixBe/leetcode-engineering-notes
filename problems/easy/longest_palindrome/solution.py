class Solution:
    def longestPalindrome(self, s: str) -> int:
        set1 = {i for i in s}
        if len(set1)==1:
            return len(s)
        l=0
        carry=0
        flag=0
        for i in set1:
            c = s.count(i)
            if c==1 and carry==0 and flag==0:
                carry=1
            elif c>1:
                if c%2==0:
                    l+=c
                else:
                    if flag==0:
                        flag=1
                        l+=c
                        carry=0
                    else:
                        l+=c-1
        return l+carry
        