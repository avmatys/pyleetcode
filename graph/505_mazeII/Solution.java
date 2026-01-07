class Solution {

    private static int[][] dirs = new int[][] {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

    private int n;
    private int m;
    private int[][] maze;
    private int[][] path;
    private int[] dest;

    private boolean isWall(int i, int j){
        if (i < 0 || i >= this.m || j < 0 || j >= this.n)
            return true;
        return this.maze[i][j] == 1;
    }

    private void dfs(int i, int j) {
        // Run in 4 dirs
        for (int[] dir: dirs) {
            int di = dir[0], dj = dir[1];
            int ni = i, nj = j;
            int rolls = this.path[i][j];
            // Roll until not wall or not a destination
            while (!isWall(ni + di, nj + dj)) {
                ni += di;
                nj += dj;
                rolls++;
            }
            // Update the length of the path to the point
            if (this.path[ni][nj] > rolls) {
                this.path[ni][nj] = rolls;
                this.dfs(ni, nj); // Try to roll futher
            }
        }
    }

    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        this.m = maze.length;
        this.n = maze[0].length;
        this.maze = maze;
        this.dest = destination;
        this.path = new int[this.m][this.n];
        for (int i = 0; i < this.m; i++) {
            Arrays.fill(this.path[i], Integer.MAX_VALUE);
        }
        // Set source equal to the zero
        int si = start[0], sj = start[1];
        this.path[si][sj] = 0;
        // Run dfs for the different possible cases
        this.dfs(si, sj);
        return this.path[this.dest[0]][this.dest[1]] != Integer.MAX_VALUE ? this.path[this.dest[0]][this.dest[1]] : -1;
    }
}
