class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Time O (M + N)
        # Space O (M + N)
        result_s = []
        result_t = []

        for c in s:
            if c == "#":
                if len(result_s) > 0:
                    result_s.pop()
            else:
                result_s.append(c)
        
        for c in t:
            if c == "#":
                if len(result_t) > 0:
                    result_t.pop() 
            else:
                result_t.append(c)

        return result_s == result_t