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

    private int i = 0; // Track the current idx in the string

    // Pay attention - this method changes i 
    private int getNumAndIncrement(String s) {
        int n = s.length();
        boolean isNeg = false;
        if (s.charAt(i) == '-') {
            isNeg = true;
            i++;
        }
        int num = 0;
        while(i < n && Character.isDigit(s.charAt(i))) {
            num = 10 * num + Integer.valueOf(s.charAt(i) - '0');
            i++;
        }
        return isNeg ? -num : num;
    }

    public NestedInteger deserialize(String s) {
        int n = s.length();
        if (i < 0 || i >= n) 
            return null;
        // New list
        if (s.charAt(i) == '['){
            i++; // Skip bracket
            NestedInteger node = new NestedInteger();
            while(i < n && s.charAt(i) != ']' ) {
                node.add(deserialize(s));
                if (s.charAt(i) == ',') 
                    i++; // Skip comma
            }
            i++; // Skip bracket
            return node;
        } 
        // Simple num
        return new NestedInteger(getNumAndIncrement(s));
    }
}
