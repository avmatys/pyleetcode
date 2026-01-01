class Solution {
    public int minimumCost(int n, int[][] connections) {
        int m = connections.length;
        if (m < n - 1) 
            return -1;
        List<int[]>[] graph = new List[n];
        for (int i = 0; i < n; i++)
            graph[i] = new ArrayList<>();
        for (int[] c: connections){
            int u = c[0] - 1, v = c[1] - 1;
            graph[v].add(new int[]{c[2], u});
            graph[u].add(new int[]{c[2], v});
        }
        Queue<int[]> q = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        boolean[] visited = new boolean[n];
        int res = 0;
        int cnt = n;
        q.offer(new int[] {0, 0});
        while (!q.isEmpty()) {
            int[] pair = q.poll();
            int cost = pair[0];
            int v = pair[1];
            if (visited[v]) 
                continue;
            cnt--;
            res += cost;
            visited[v] = true;
            if (cnt == 0)
                return res;
            for (int[] nei: graph[v]) {
                if (visited[nei[1]]) 
                    continue;
                q.offer(nei);
            }
        }
        return -1;
    }
}
