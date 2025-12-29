class Solution {

    private final int[][] dir = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

    private int[][] grid;
    private int[] roots;
    private int n;

    private boolean isValid(int i, int j) {
        return i >= 0 && i < this.n && j >= 0 && j < this.n && this.grid[i][j] > 0;
    }

    private long dfs(int i, int j, boolean[][] visited, int root) {
        if (visited[i][j]) 
            return 0;
        visited[i][j] = true;
        this.roots[this.getIdx(i, j)] = root; // Store the cell from which dfs was started
        long csum = this.grid[i][j];
        for (int[] d : dir) {
            int ni = d[0] + i;
            int nj = d[1] + j;
            if (!this.isValid(ni, nj)) 
                continue;
            csum += dfs(ni, nj, visited, root);
        }
        return csum;
    }

    private int getIdx(int i, int j) {
        return this.n * i + j;
    }

    public long sumRemoteness(int[][] grid) {
        this.grid = grid;
        this.n = grid.length;
        int n2 = this.n * this.n;
        this.roots = new int[n2];
        for(int i = 0; i < n2; i++) {
            this.roots[i] = i;
        }
        boolean[][] visited = new boolean[this.n][this.n];
        long[] components = new long[n2];
        long totalSum = 0;
        for (int i = 0; i < this.n; i++){
            for (int j = 0; j < this.n; j++) {
                if (this.grid[i][j] < 0 || visited[i][j]) 
                    continue;
                int componentIdx = this.getIdx(i, j);
                long componentSum = dfs(i, j, visited, componentIdx);
                components[componentIdx] = componentSum;
                totalSum += componentSum;
            }
        }
        long result = 0;
        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.n; j++) {
                if (this.grid[i][j] < 0) 
                    continue;
                int idx = this.getIdx(i, j);
                result += totalSum - components[this.roots[idx]];
            }
        }
        return result;
        
    }
}
