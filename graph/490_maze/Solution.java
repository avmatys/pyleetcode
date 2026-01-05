class Solution {

    private final static int[][] DIRS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    private int[][] maze;
    private int[][] seen;
    private int[] dest;
    private int n;
    private int m;

    private boolean isWall(int i, int j){
        if (i < 0 || i >= this.m || j < 0 || j >= this.n)
            return true;
        return this.maze[i][j] == 1;
    }

    private boolean dfs(int i, int j, int di, int dj) {
        if (i < 0 || i >= this.m || j < 0 || j >= this.n)
            return false;
        // We can change a direction if needed
        if (this.isWall(i + di, j + dj) || (di == -1 && dj == -1)) {
            // Ball reached the destination
            if (i == this.dest[0] && j == this.dest[1]) 
                return true;
            // Change direction of the ball
            for (int b = 0; b < 4; b++) {
                // Check b-th bit of the seen
                if (((seen[i][j] >> b) & 1) == 0) {
                    seen[i][j] |= (1 << b); // Mark as visited
                    if (dfs(i, j, DIRS[b][0], DIRS[b][1]))
                        return true;
                }
            }    
        } else {
            // Just move futher
            return dfs(i + di, j + dj, di, dj);
        }
        // Non reachable dest
        return false;
    }

    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        this.maze = maze;
        this.dest = destination;
        this.m = maze.length;
        this.n = maze[0].length;
        this.seen = new int[m][n];
        return dfs(start[0], start[1], -1, -1);
    }
}
