class Solution {

    private static int[] dirs = {1, 0, -1, 0, 1};

    public int[][] updateMatrix(int[][] mat) {
        Queue<int[]> q = new LinkedList<>();
        int m = mat.length, n = mat[0].length;
        int[][] result = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    q.offer(new int[] {i, j});
                    result[i][j] = 0;
                } else {
                    result[i][j] = -1; // Not processed yet
                }
            }
        }
        while(!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0) {
                int[] entry = q.poll();
                int i = entry[0], j = entry[1];
                int v = result[i][j]; // Get the latest value
                for (int d = 0; d < dirs.length - 1; d++) {
                    int ni = i + dirs[d], nj = j + dirs[d+1]; 
                    if (0 <= ni && ni < m && 0 <= nj && nj < n && result[ni][nj] == -1) {
                        result[ni][nj] = v + 1;
                        q.offer(new int[] {ni, nj});
                    }
                }
            }
        }
        return result;
    }
}
