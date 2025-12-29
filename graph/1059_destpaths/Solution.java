class Solution {

    private List<Integer>[] graph;
    private int dest;

    private boolean dfs(int node, boolean[] seen, boolean[] proc) {
        if (proc[node]) return false; // cycle detected
        if (seen[node]) return true; // node was processed
        if (this.graph[node].isEmpty())
            return node == dest; // check if node with out degree 0 is a dest
        proc[node] = true;
        seen[node] = true;
        for (int nei: this.graph[node]) {
            if (!this.dfs(nei, seen, proc)) {
                return false;
            }
        }
        proc[node] = false; // backtracking
        return true;
    }

    public boolean leadsToDestination(int n, int[][] edges, int source, int destination) {
        dest = destination;
        graph = new List[n];
        for (int i = 0; i < n; i++){
            graph[i] = new ArrayList<>();
        }
        for(int[] edge: edges){
            graph[edge[0]].add(edge[1]);
        }
        boolean[] seen = new boolean[n]; // Completely processed
        boolean[] proc = new boolean[n]; // In process
        return dfs(source, seen, proc);      
    }
}
