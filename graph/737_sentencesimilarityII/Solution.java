class Solution {
    public boolean areSentencesSimilarTwo(String[] sentence1, String[] sentence2, List<List<String>> similarPairs) {

        class UnionFind {

            Map<String, String> root = new HashMap<>();

            public String find(String x) {
                if (!root.containsKey(x)) root.put(x, x);
                while (x != root.get(x)){
                    x = root.get(x);
                }
                return x;
            }

            public void union(String x, String y){
                if (!root.containsKey(x)) root.put(x, x); // Lazy init
                if (!root.containsKey(y)) root.put(y, y); // Lazy init
                String px = find(x);
                String py = find(y);
                if (px != py) {
                    root.put(py, px);
                }
            }

            public boolean isConnected(String x, String y){
                return find(x) == find(y);
            }
        }

        int n1 = sentence1.length;
        int n2 = sentence2.length;
        if (n1 != n2) 
            return false;

        UnionFind uf = new UnionFind();
        for (List<String> edge: similarPairs) {
            uf.union(edge.get(0), edge.get(1));
        }

        for (int i = 0; i < n1; i++) {
            if(!uf.isConnected(sentence1[i], sentence2[i]))
                return false;
        }
        return true;
        
    }
}
