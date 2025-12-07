class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        # O (N) O (1)
        # FLLLLL FL
        # FLY FLORIDA
        # "" FL
        prev = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]
            for j in range(len(word)):
                c = word[j]
                if len(prev) - 1 < j:
                    break
                if prev[j] != c:
                    prev = prev[:j]
                    break
            # if previous word is longer than current word
            prev = prev[0:len(word)]
        
        return prev
