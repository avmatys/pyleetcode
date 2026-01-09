class Solution {

    Map<Integer,Integer> vals;

    private int[] getChilds(int node) {
        int level = node / 10;
        int place = node % 10;
        int left = 10 *(level + 1) + 2* place - 1;
        int right = 10 *(level + 1) + 2* place;
        return new int[] { left, right };
    }

    private int dfs(int node, int prevSum) {
        if (!vals.containsKey(node)) 
            return 0;
        int currSum = prevSum + vals.get(node);
        int[] childs = this.getChilds(node);
        if (!vals.containsKey(childs[0]) && !vals.containsKey(childs[1])){
            return currSum;
        }
        return dfs(childs[0], currSum) + dfs(childs[1], currSum);
    }


    public int pathSum(int[] nums) {
        vals = new HashMap<>();
        for (int val: nums) {
            vals.put(val / 10, val % 10);
        }
        return dfs(11, 0);
    }
}
