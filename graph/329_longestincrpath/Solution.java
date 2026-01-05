class Solution {

    private int[][] DIRS = new int[][] {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    private int n;
    private int m;
    private int[][] memo;
    private int[][] matrix;

    private int dfs(int i, int j) {
        if (memo[i][j] != -1) 
            return memo[i][j];
        memo[i][j] = 1;
        for (int[] dir: this.DIRS) {
            int i1 = i + dir[0], j1 = j + dir[1];
            if (i1 < 0 || i1 >= m || j1 < 0 || j1 >= n || matrix[i1][j1] <= matrix[i][j])
                continue;
            memo[i][j] = Math.max(memo[i][j], 1 + dfs(i1, j1));
        }
        return memo[i][j];
    }

   
    public int longestIncreasingPath(int[][] matrix) {
        this.m = matrix.length;
        this.n = matrix[0].length;
        this.memo = new int[m][n];
        this.matrix = matrix;
        for (int i = 0; i < m; i++)
            Arrays.fill(memo[i], -1);
        int res = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res = Math.max(res, dfs(i, j));
            }
        }
        return res;
    }
}
