public class Solution {
    public int MaxProduct(int[] nums) {
        // set 2 variables with the first index value
        // Time Complexity O(N) and Auxilary space will be O(1)
        int maxProduct = nums[0];

        int globalMax = nums[0];
        int globalMin = nums[0];

        for (int i=1; i < nums.Length; i++){
            int localMax = globalMax * nums[i];
            int localMin = globalMin * nums[i];

            globalMax = Math.Max(localMin, localMax);
            globalMax = Math.Max(nums[i], globalMax);

            globalMin = Math.Min(localMin, localMax);
            globalMin = Math.Min(nums[i], globalMin);

            maxProduct = Math.Max(maxProduct, globalMax);
        }

        return maxProduct;

    }
}