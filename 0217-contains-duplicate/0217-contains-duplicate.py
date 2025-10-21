class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # easiest way time O (N) Space O (N)
        dic = {}

        for n in nums:
            if n in dic:
                return True

            dic[n] = 1 + dic.get(n, 0)

        return False