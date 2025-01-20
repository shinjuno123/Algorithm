class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4,5,6,7,0,1,2,d,d,d,d
        # target = 5
        # 2,3,4,5,1
        # target = 3
        # Time complexity O(log N) Space O(1)
        # mid = left + (right - left) / 2 
        left: int = 0
        right: int = len(nums) - 1
        pivot = 0

        while left <= right:
            mid = (right - left) // 2 + left

            if nums[right] < nums[mid]:
                left = mid + 1
            elif nums[right] > nums[mid]:
                right = mid
            else:
                pivot = mid
                break
        
        left = pivot
        right = (pivot - 1) + len(nums)

        while left <= right:
            mid = (right - left) // 2 + left
            actual_mid = mid % len(nums)

            if nums[actual_mid] < target:
                left = mid + 1
            elif nums[actual_mid] > target:
                right = mid - 1
            else:
                return actual_mid

        return -1
        