class Solution:
    def trap(self, height: List[int]) -> int:
        # Time complexity is O (N)
        # Auxilary Space Complexity O (1)
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        total_water = 0

        while left < right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)

            if height[left] <= height[right]:
                current_water = max_left - height[left]
                total_water += current_water
                left += 1
            else:
                current_water = max_right - height[right]
                total_water += current_water
                right -= 1
        
        return total_water

