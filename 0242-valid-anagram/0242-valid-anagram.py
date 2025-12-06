class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # O (M + N) O (M)
        hashed = {}

        for c in s:
            hashed[c] = 1 + hashed.get(c, 0)
        
        for c in t:
            if c not in hashed or c in hashed and hashed[c] == 0:
                return False

            hashed[c] -= 1

        return True