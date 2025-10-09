class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Time O (N + M), Space O (N)
        storage = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in storage:
                storage[ransomNote[i]] = 1
            else:
                storage[ransomNote[i]] += 1
        
        for i in range(len(magazine)):
            if magazine[i] in storage and storage[magazine[i]] > 0:
                storage[magazine[i]] -= 1

        return not any(storage.values())
        