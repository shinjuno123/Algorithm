public class Solution {
    public int MaxProfit(int[] prices) {
        // O(N) solution

        int min = Int32.MaxValue; // the lowest point 
        int profit = 0; // we don't want minus profit so fix it at 0.

        for (int i=0; i<prices.Length; i++) {
            // Even lower the lowest point
            min = Math.Min(min, prices[i]);
            // maximize the profit
            profit = Math.Max(prices[i] - min, profit);
        }

        return profit;
    }
}