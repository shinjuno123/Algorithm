class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4,5,6,7,0,1,2
        # Time complexity O(N) Space O(1)
        # Iterate over the list and check where the target is
        # When we found the target, we will return the index number right away
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i

        return -1