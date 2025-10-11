class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O (N) O (N)
        dic = {}
        max_val = float('-inf')
        max_key = None

        for num in nums:
            dic[num] = 1 + dic.get(num, 0)

            if max_val < dic[num]:
                max_val = dic[num]
                max_key = num

        return max_key