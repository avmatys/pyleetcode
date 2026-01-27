class Solution {
    public int deleteAndEarn(int[] nums) {
        int[] freq = new int[10001];
        int max = 0;
        for (int x: nums) {
            freq[x] += 1;
            max = Math.max(max, x);
        }
        int twoBack = 0;
        int oneBack = freq[1];
        for (int i = 2; i < max + 1; i++) {
            int tmp = oneBack;
            oneBack = Math.max(freq[i] * i + twoBack, oneBack);
            twoBack = tmp;
        }
        return oneBack;
    }
}
