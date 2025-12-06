class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        h_w = 0
        for digit in binary:
            if digit == "1":
                h_w += 1
        return h_w