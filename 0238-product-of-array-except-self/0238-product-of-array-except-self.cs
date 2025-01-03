public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        // O(N^2) Time and O(N) space Brute force 
        // int[] results = new int[nums.Length];
        // Array.Fill(results, 1);

        // for (int i=0; i<nums.Length; i++) {
        //     for (int j=0; j<nums.Length; j++) {
        //         if (i == j) {
        //             continue;
        //         }

        //         results[i] *= nums[j];
        //     }
        // }

        // return results;

        // O (N) time and O (1) extra space solution
        // Actually this solution was O(1) space solution
        // Because we only return the same amount of the array as we received and didn't use auxilary space.
        int[] results = new int[nums.Length];
        int start = 1;

        for (int i=0; i< nums.Length; i++) {
            if (i == 0) {
                results[i] = start;
                continue;
            }

            start *= nums[i-1];
            results[i] = start;
        }

        start = 1;

        for (int i=nums.Length - 1; i >= 0; i--) { 
            if (i == nums.Length - 1) {
                results[i] = start * results[i];
                continue;
            }

            start *= nums[i + 1];
            results[i] = start * results[i];
        }

        return results;
    }
}