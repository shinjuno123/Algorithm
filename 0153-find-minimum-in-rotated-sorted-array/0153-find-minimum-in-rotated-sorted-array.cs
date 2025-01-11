public class Solution {
    public int FindMin(int[] nums) {
        // It says that the algorithm should run O (log n) times.
        // We need to use binary search for that
        int left = 0;
        int right = nums.Length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return nums[left];
    }
}