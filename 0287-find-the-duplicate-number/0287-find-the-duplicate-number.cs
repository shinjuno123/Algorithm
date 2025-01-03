public class Solution {
    public int FindDuplicate(int[] nums) {
        // Space O(n), Time O(n)
        // Dictionary<int, int> memory = new Dictionary<int,int>();

        // for (int i=0;i<nums.Length;i++) {
        //     if (!memory.ContainsKey(nums[i])) {
        //         memory.Add(nums[i], 0);
        //     } else {
        //         return nums[i];
        //     }
        // }

        // return 0;


        // Space O(1), Time O(N)
        // We can't save any duplicate number in the list or dict since that would cost O(n) space.
        
        // After analyzing the floyd's circle, I found that if I treat the input array as a linked list
        // I set up tortoise and hare to traverse over the array. Then a cycle will happen for tortoise and hare both
        // Then, I put the slow pointer back to the first
        // Lastly, traverse slow pointer and fast pointer in the same speed
        // Fast pointer will already be in the cycle so eventually, the slow and fast pointer will meet at the same point
        // which is the duplicate number

        int fast = nums[0], slow = nums[0];

        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        slow = nums[0];

        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }

        return slow;
    }
}