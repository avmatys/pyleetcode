class Solution {

    private List<int[]> storage = new ArrayList<>();
    private int n;

    private void backtrack(int[] seq, boolean[] used, int i) {
        if (i == this.n) {
            this.storage.add(seq.clone());
            return;
        }
        for (int x = 1; x < n + 1; x++) {
            if (used[x]) 
                continue;
            if (i == 0 || seq[i-1] % 2 != x % 2) {
                seq[i] = x;
                used[x] = true;
                backtrack(seq, used, i + 1);
                used[x] = false;
            }
        }
    }

    public int[][] permute(int n) {
        this.n = n;
        int[] seq = new int[n];
        boolean[] used = new boolean[n + 1];
        backtrack(seq, used, 0);
        int[][] result = new int[this.storage.size()][n];
        for (int i = 0; i < result.length; i++) {
            result[i] = this.storage.get(i);
        }
        return result;
    }
}
