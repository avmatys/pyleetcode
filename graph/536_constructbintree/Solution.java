/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    private int i = 0;
    private String s;

    private TreeNode dfs() {
        int n = s.length();
        if (i < 0 || i >= n) 
            return null;
        boolean isNeg = s.charAt(i) == '-';
        if (isNeg) i++;
        int num = 0;
        while (i < n && Character.isDigit(s.charAt(i))) {
            num = 10 * num + Integer.valueOf(s.charAt(i) - '0');
            i++;
        }
        if (isNeg) num = -num;
        TreeNode node = new TreeNode(num);
        if (i < n && s.charAt(i) == '(' ) {
            i++; // Skip (
            node.left = dfs();
            i++; // Skip )
        }
        if (i < n && s.charAt(i) == '(' ) {
            i++; // Skip (
            node.right = dfs();
            i++; // Skip )
        }
        return node;
    }

    public TreeNode str2tree(String s) {
        this.i = 0;
        this.s = s;
        return dfs();
    }
}
