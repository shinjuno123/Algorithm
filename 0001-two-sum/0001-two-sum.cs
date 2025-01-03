public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // O(n^2)

        // for (int i=0; i < nums.Length; i++) {
        //     for (int j=i+1;j <nums.Length;j++){
        //         if (nums[i] + nums[j] == target) {
        //             return new int[] {i, j};
        //         }
        //     }
        // }

        // return new int[] {};


        // O(n)

        Dictionary<int, int> savedMap = new Dictionary<int, int>();

        for (int i=0; i<nums.Length; i++) {

            int complement = target - nums[i];

            if (savedMap.ContainsKey(complement)) {
                return new int[] {savedMap[complement], i};
            } 

            if (!savedMap.ContainsKey(nums[i])) {
                savedMap.Add(nums[i], i);
            }
        }

        return new int[] {};
    }
}