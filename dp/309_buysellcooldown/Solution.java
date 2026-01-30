class Solution {

    private int[][] dp;
    private int[] prices;
    private int n;

    // State
    // 0 = don't have a stock
    // 1 = have a stock
    // 2 = cooldown
    private int solve(int curr, int hold) {
        if (curr >= n) {
            return 0;
        }
        if (dp[curr][hold] == Integer.MIN_VALUE) {
            if (hold == n) { // Don't have a stock
                dp[curr][hold] = Math.max(
                                    solve(curr + 1, curr), // buy
                                    solve(curr + 1, n) // skip
                                );
            }
            else {
                dp[curr][hold]= Math.max(
                                    prices[curr] - prices[hold] + solve(curr + 2, n),
                                    solve(curr + 1, hold) // hold curr
                                ); 
            }
        }
        return dp[curr][hold];
    }

    public int maxProfit(int[] prices) {
        this.prices = prices;
        this.n = prices.length;
        this.dp = new int[n][n + 1];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], Integer.MIN_VALUE);
        }
        return solve(0, n);
        
    }
}
