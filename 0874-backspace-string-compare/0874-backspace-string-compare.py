class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ps, pt = len(s) - 1, len(t) - 1

        def get_next_valid_pointer(s, end):
            backspace_count = 0
            while end >= 0:
                if s[end] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                
                end -= 1
            
            return end

        while ps >= 0 or pt >= 0:
            ps = get_next_valid_pointer(s, ps)
            pt = get_next_valid_pointer(t, pt)

            if ps < 0 and pt < 0:
                return True
            elif ps < 0 or pt < 0:
                return False
            elif s[ps] != t[pt]:
                return False
        
            ps -= 1
            pt -= 1
            
        return True