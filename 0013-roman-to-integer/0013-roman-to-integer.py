class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prev = 0
        total = 0

        for c in s:
            if roman_map[c] > prev:
                total += roman_map[c] - (prev * 2)
            else:
                total += roman_map[c]
            prev = roman_map[c]
        
        return total