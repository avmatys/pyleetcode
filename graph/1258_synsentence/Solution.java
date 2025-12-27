class Solution {

    private List<String> result = new ArrayList<>();
    private UnionFind uf;
    private Map<String, List<String>> groups;

    class UnionFind {
        private Map<String, String> roots;
    
        public UnionFind() {
            this.roots = new HashMap<>();
        }

        public String find(String x){
            this.roots.putIfAbsent(x, x);
            if (this.roots.get(x) == x)
                return x;
            this.roots.put(x, this.find(this.roots.get(x)));
            return this.roots.get(x);
        }

        public void union(String x, String y) {
            String px = this.find(x);
            String py = this.find(y);
            if (!px.equals(py))
                this.roots.put(py, px);
        }

        public Map<String, List<String>> getAllGroups() {
            Map<String, List<String>> result = new HashMap<>();
            for (String node: this.roots.keySet()){
                String parent = this.find(node);
                result.putIfAbsent(this.find(node), new ArrayList());
                result.get(parent).add(node);
            }
            for (String key: result.keySet()) {
                Collections.sort(result.get(key));
            }
            return result;
        }
    }

    private void backtrack(String[] current, int i) {
        int n = current.length;
        if (i == n) {
            result.add(String.join(" ", current));
            return;
        }
        String root = uf.find(current[i]);
        if (groups.containsKey(root)) {
            for (String synonym: groups.get(root)){
                String tmp = current[i];
                current[i] = synonym;
                backtrack(current, i + 1);
                current[i] = tmp;
            }
        } else {
            backtrack(current, i + 1);
        } 
    }

    public List<String> generateSentences(List<List<String>> synonyms, String text) {
        this.uf = new UnionFind();
        for (List<String> pair: synonyms) {
            this.uf.union(pair.get(0), pair.get(1));
        }
        this.groups = uf.getAllGroups();
        System.out.println(groups);
        String[] current = text.split("\\s+");
        this.backtrack(current, 0);
        return this.result;
    }
}
