class Solution {

     class UnionFind {
        int[] roots;
        int n;
        int rootCount;

        public UnionFind(int n){
            this.roots = new int[n];
            for (int i = 0; i < n; i++){
                this.roots[i] = i;
            }
            this.n = n;
            this.rootCount = n;
        }

        public int find(int x){
            return this.roots[x];
        }

        public void union(int x, int y){
            int px = this.find(x);
            int py = this.find(y);
            for(int i = 0; i < this.n && px != py; i++){
                if (this.roots[i] == py){
                    if (this.roots[i] == i)
                        this.rootCount -= 1;
                    this.roots[i] = px;
                }
            }
        }

        public int getRootCount(){
            return this.rootCount;
        }

    }

    public int earliestAcq(int[][] logs, int n) {
        Arrays.sort(logs, Comparator.comparingInt(o -> o[0]));
        UnionFind uf = new UnionFind(n);
        for(int[] log: logs){
            uf.union(log[1], log[2]);
            if (uf.getRootCount() == 1) 
                return log[0];
        }
        return -1;
    }
}
