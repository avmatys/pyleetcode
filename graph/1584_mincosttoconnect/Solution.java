class Solution {

    class UnionFind {
        private int components;
        private int[] roots;
        private int[] ranks;

        public UnionFind(int n) {
            this.components = n;
            this.roots = new int[n];
            this.ranks = new int[n];
            for (int i = 0; i < n; i++) {
                this.roots[i] = i;
                this.ranks[i] = 1;
            }
        }

        public int find(int x){
            if (x == this.roots[x]) 
                return x;
            this.roots[x] = this.find(this.roots[x]);
            return this.roots[x];
        }

        public boolean union(int x, int y){
            int px = this.find(x);
            int py = this.find(y);
            if (px == py) 
                return false;
            if (this.ranks[px] > this.ranks[py]) {
                this.roots[px] = py;
                this.ranks[py] += this.ranks[px];
            } else {
                this.roots[py] = px;
                this.ranks[px] += this.ranks[py];
            }
            this.components--;
            return true;
        }

        public int getComponentsCount() {
            return this.components;
        }
    }

    public int minCostConnectPoints(int[][] points) {
        List<int[]> weights = new ArrayList<>();
        int n = points.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int weight = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                weights.add(new int[] {i, j, weight});
            }
        }
        Collections.sort(weights, (w1, w2) -> w1[2] - w2[2]);
        UnionFind uf = new UnionFind(n);
        int result = 0;
        for (int[] w: weights) {
            if (uf.union(w[0], w[1]))
                result += w[2];
            if (uf.getComponentsCount() == 1) 
                break;
        }
        return result;
    }
}
