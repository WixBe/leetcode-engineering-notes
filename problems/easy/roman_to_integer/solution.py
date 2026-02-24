class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        n = 0
        prev = 0
        for i in s:
            match i:
                case 'M': n = 1000
                case 'D': n = 500
                case 'C': n = 100
                case 'L': n = 50
                case 'X': n = 10
                case 'V': n = 5
                case 'I': n = 1
            if n > prev:
                res += n - 2 * prev
            else:
                res += n
            prev = n
        return res
        