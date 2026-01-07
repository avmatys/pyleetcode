class Solution {

    private static int[][] dirs = new int[][] {{0,1},{0,-1},{1,0},{-1,0}};
    private static String[] inst = new String[] {"r", "l", "d", "u"};

    private boolean isPath(int[][] maze, int i, int j) {
        int m = maze.length, n = maze[0].length;
        return i >= 0 && i < m && j >= 0 && j < n && maze[i][j] == 0;
    }

    private String dijkstra(int[][] maze, int[] source, int[] dest) {
        int m = maze.length, n = maze[0].length;
        // Distances to the point
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++)
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        dist[source[0]][source[1]] = 0;
        // Paths to the point
        String[][] path = new String[m][n];
        path[source[0]][source[1]] = "";
        // Heap for the shortest distance
        Queue<int[]> queue = new PriorityQueue<>((a,b) -> {return Integer.compare(a[0],b[0]);});
        queue.offer(new int[] {0, source[0], source[1]});
        while(!queue.isEmpty()) {
            int[] top = queue.poll();
            int cdist = top[0];
            int i = top[1];
            int j = top[2];
            // We already have a better solution
            if (cdist > dist[i][j])
                continue;
            // Try 4 directions
            for (int k = 0; k < dirs.length; k++) {
                int di = dirs[k][0];
                int dj = dirs[k][1];
                int ni = i;
                int nj = j;
                int ndist = cdist;
                // Roll ball until it's path and stop if it's a hole
                while (isPath(maze, ni + di, nj + dj)){
                    ni += di;
                    nj += dj;
                    ndist++;
                    if (ni == dest[0] && nj == dest[1]) 
                        break;
                }
                String npath = path[i][j] + inst[k];
                // Add to the queue if dist is smaller or path is smaller
                if (ndist < dist[ni][nj] || (ndist == dist[ni][nj] && npath.compareTo(path[ni][nj]) < 0)) {
                    path[ni][nj] = npath;
                    dist[ni][nj] = ndist;
                    queue.offer(new int[] {ndist, ni, nj});
                } 
            }
        }
        // Check if hole reachable
        return path[dest[0]][dest[1]] != null ? path[dest[0]][dest[1]] : "impossible";
    }

    public String findShortestWay(int[][] maze, int[] ball, int[] hole) {
        return dijkstra(maze, ball, hole);
    }
}
