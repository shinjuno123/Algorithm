class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # get current water amount based on the left and right lines
            current_water = (right - left) * min(height[left],height[right])

            # get max water amount
            max_water = max(max_water, current_water)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        
        return max_water


