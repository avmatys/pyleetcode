/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Solution {

    class Pair {
        NestedInteger val;
        int depth;
        public Pair(NestedInteger val, int depth) {
            this.depth = depth;
            this.val = val;
        }
    }

    public int depthSumInverse(List<NestedInteger> nestedList) {
        // Calc max depth and store flat values to the array
        int maxDepth = 0;
        Stack<Pair> stack = new Stack<>();
        for(NestedInteger ni: nestedList)
            stack.push(new Pair(ni, 1));
        List<Pair> allVals = new ArrayList<>();
        while (!stack.isEmpty()) {
            Pair top = stack.pop();
            if (top.val.isInteger()) {
                maxDepth = Math.max(maxDepth, top.depth);
                allVals.add(top);
                continue;
            }
            for(NestedInteger ni: top.val.getList()){
                stack.push(new Pair(ni, top.depth + 1));
            }
        }
        // Get sum of weights
        int weightSum = 0;
        for (Pair p: allVals) 
            weightSum += (maxDepth - p.depth + 1) * p.val.getInteger();
        return weightSum;
    }
}
