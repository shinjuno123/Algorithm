class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            b = bin(i)[2:]
            total = 0
            for number_string in b:
                total += int(number_string)
            
            ans.append(total)
        return ans
            