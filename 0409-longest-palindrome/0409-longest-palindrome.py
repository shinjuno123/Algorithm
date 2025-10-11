class Solution:
    def longestPalindrome(self, s: str) -> int:
        bank = {}
        result = 0

        for c in s:
            bank[c] = 1 + bank.get(c, 0)
        
        for v in bank.values():
            result += v if v % 2 == 0 else v - 1
        
        return result + 1 if result < len(s) else result

