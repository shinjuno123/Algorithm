class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        results = []
        for i in range(len(words) -1, -1, -1):
            results.append(words[i])
        
        return " ".join(results)