class Solution {

    class UnionFind {
        private int[] roots;

        UnionFind() {
            roots = new int[26];
            for (int i = 0; i < 26; i++)
                roots[i] = i;
        }

        void union(int x, int y){
            int px = find(x);
            int py = find(y);
            if (px != py) 
                roots[py] = px;
        }
        int find(int x){
            if (roots[x] != x)
                roots[x] = find(roots[x]);
            return roots[x];
        }
        boolean isConnected(int x, int y){
            return find(x) == find(y);
        }
    }
    public boolean equationsPossible(String[] equations) {
        UnionFind uf = new UnionFind();
        for(String item: equations){
            if (item.charAt(1) == '='){
                int x = (int)item.charAt(0) - 97;
                int y = (int)item.charAt(3) - 97;
                uf.union(x, y);
            }
        }
        for(String item: equations){
            if (item.charAt(1) == '!'){
                int x = (int)item.charAt(0) - 97;
                int y = (int)item.charAt(3) - 97;
                if(uf.isConnected(x, y)) {
                    return false;
                }
            }
        }
        return true;
    }
}
