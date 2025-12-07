class Solution {

    class UnionFind {
        private int[] root;
        
        public UnionFind(int size) {
            this.root = new int[size];
            for(int i=0; i < size; i++) {
                this.root[i] = i;
            }
        }

        public int find(int x){
            while (x != this.root[x])
                x = this.root[x];
            return x;
        }

        public boolean isConnected(int x, int y) {
            return this.find(x) == this.find(y);
        }

        public void union(int x, int y) {
            int px = this.find(x);
            int py = this.find(y);
            if (px != py) {
                this.root[py] = px;
            }
        }
    }

    public int[] findRedundantConnection(int[][] edges) {
        UnionFind uf = new UnionFind(edges.length + 1);
        for (int[] edge: edges) {
            if (uf.isConnected(edge[0], edge[1])){
                return edge;
            }
            uf.union(edge[0], edge[1]);
        }
        return new int[2];
    }
}
