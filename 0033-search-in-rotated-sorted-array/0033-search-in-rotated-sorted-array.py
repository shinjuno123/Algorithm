class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left
            
            # If target is already at the mid, 
            if nums[mid] == target:
                # return it
                return mid
            
            # If left half is sorted
            elif nums[left] <= nums[mid]:
                # Check if target is lying in the left side
                if nums[left] <= target < nums[mid]:
                    # move right pointer to left side
                    right = mid - 1
                # if target is lying in the right side
                else:
                    # move the left pointer to the right side
                    left = mid + 1
            # If right half is sorted
            else:
                # check if the target is lying in the right side
                if nums[mid] < target <= nums[right]:
                    # Move the left pointer to the right side
                    left = mid + 1
                # if target is lying in the left side
                else:
                    # Move the right pointer to the left side
                    right = mid - 1
        
        return -1
        