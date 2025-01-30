class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Time complexity O(N!)
        # Limit exceeds
        # if n <= 4:
        #     return 0

        # fac = 0
        # for i in range(n, 0, -1):
        #     if i == n:
        #         fac = i
        #         continue

        #     fac *= i

        # fac = str(fac)
        # count = 0

        # for i in range(len(fac)-1,-1,-1):
        #     if fac[i] == '0':
        #         count += 1
        #     else:
        #         break

        # return count

        # 5! = 120
        # 6! = 720
        # 7! = 5040
        # 8! = count 1
        # 9! = count 1
        # 10! = count 2

        # 2 * 5 = 10
        # there are always more 2 than 5 in a factorial, the number of trailing zeroes is determined by the number of 5

        count = 0
        
        while n >= 5:
            n = n // 5
            count += n
        
        return count