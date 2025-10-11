class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            dic[num] = 1 + dic.get(num, 0)
        
        max_val = float('-inf')
        max_key = None

        for key in dic:
            if max_val < dic[key]:
                max_val = dic[key]
                max_key = key

        return max_key