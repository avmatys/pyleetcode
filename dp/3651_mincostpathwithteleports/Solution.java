class Solution {

    /*
        1 3 3 
        2 5 4 
        4 3 5
    */

    // Base case solver
    // To solve the whole grid - start with 0, 0
    private void base(int[][] grid, int[][] memo) {
        int m = grid.length;
        int n = grid[0].length;
        for (int i = 1; i < m; i++) 
            memo[i][0] = Math.min(memo[i - 1][0] + grid[i][0], memo[i][0]);
        for (int j = 1; j < n; j++) 
            memo[0][j] = Math.min(memo[0][j - 1] + grid[0][j], memo[0][j]);
        for (int i =  1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                memo[i][j] = Math.min(memo[i][j], grid[i][j] + Math.min(memo[i-1][j], memo[i][j-1]));
            }
        }
    }

    // Solve case with k
    private void optimize(int[][] grid, int[][] memo, int[][] flat) {
        int n = flat.length;
        int minWeight = Integer.MAX_VALUE;
        for (int i = 0, j = 0; i < n; i++) {
            minWeight = Math.min(memo[flat[i][0]][flat[i][1]], minWeight);
            if (i + 1 < n && grid[flat[i+1][0]][flat[i+1][1]] == grid[flat[i][0]][flat[i][1]])
                continue;
            for (int l = j; l <= i; l++)
                memo[flat[l][0]][flat[l][1]] = minWeight;
            j = i + 1;
        }
    }

    public int minCost(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] memo = new int[m][n];
        for (int i = 0; i < m; i++)
            Arrays.fill(memo[i], Integer.MAX_VALUE);
        memo[0][0] = 0;
        // Prepare a flat list of values with indexes
        int[][] flat = new int[m * n][2];
        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                flat[n*i + j] = new int[] { i, j };
            }
        }
        // Sort ascending
        Arrays.sort(flat, (a, b) -> -Integer.compare(grid[a[0]][a[1]], grid[b[0]][b[1]]));
        // Solve with k = 0
        base(grid, memo);
        // Optimize k times
        for (int i = 1; i <= k; i++) {
            optimize(grid, memo, flat);
            base(grid, memo);
        }
        return memo[m - 1][n - 1];
    }
}
