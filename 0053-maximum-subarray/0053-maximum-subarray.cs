public class Solution {
    public int MaxSubArray(int[] nums) {
        // // Time complexity O(n^2) Auxilary Space Complexity O(1)
        // // initialize the maximum value
        // // Time Limit exceeded
        // int max = int.MinValue;

        // // Iterate over the array
        // // Find the maximum sum that reflects the maximum subarray.
        // for (int i=0; i<nums.Length; i++) {
        //     int currentSum = 0;
        //     for (int j=i; j<nums.Length; j++) {
        //         currentSum += nums[j];
        //         // Maximize the sum
        //         max = Math.Max(currentSum, max);
        //     }
        // }

        // return max;

        // Time complexity O(n) Space Complexity O (1)
        // So... in the array, I see that the positive value and negative values are all mixed
        // We can consider that the maximized sum will be in positive.

        int max = nums[0];
        int sum = nums[0];

        for (int i=1;i<nums.Length;i++) {
            // If the sum is lower than 0 then just reset it to 0
            // since negative value is not helpful for the maximized sum.
            if (sum < 0) {
                sum = 0;
            }

            // Add the value at the current index to the sum
            sum += nums[i];
            // get the maximized sum on each iteration
            max = Math.Max(sum, max);
        }


        return max;
    }
}