class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = majority = 0

        for n in nums:
            if majority == 0:
                res = n
            
            if n == res:
                majority += 1
            else:
                majority -= 1

        return res