class Solution:
    def addBinary(self, a: str, b: str) -> str:
        over = 0
        result = []
        if len(a) < len(b):
            return self.addBinary(b, a)
        
        b = "0" * (len(a) - len(b)) + b
        
        # a is always longer than or equal to the length of b

        for i in range(len(a) - 1, -1, -1):
            a_digit = int(a[i])
            b_digit = int(b[i]) if len(b) > i else 0
            current_digit_sum = a_digit + b_digit + over
            if current_digit_sum >= 2:
                over = 1
                result.append(str(current_digit_sum - 2))
            else:
                over = 0
                result.append(str(current_digit_sum))
        
        if over > 0:
            result.append(str(over))
            over = 0
        
        return ''.join(reversed(result))
            