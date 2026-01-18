class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int flipIdx = -1;
        int res = 0;
        int l = 0;
        for (int r = 0; r < nums.length; r++) {
            if (nums[r] == 0) {
                if (flipIdx != -1) {
                    l = flipIdx;
                }
                flipIdx = r + 1; // Next after the 0
            }
            res = Math.max(res, r - l + 1);
        }
        return res; 
    }
}
