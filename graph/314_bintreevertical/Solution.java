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

    class Pair {
        TreeNode node;
        int column;

        public Pair(TreeNode node, int column) {
            this.node = node;
            this.column = column;
        }
    }

    private List<Integer>[] columns;

    private void bfs(TreeNode node) {
        if (node == null) 
            return;
        Deque<Pair> q = new LinkedList<>();
        q.addLast(new Pair(node, 50));
        while(!q.isEmpty()) {
            Pair p = q.pollFirst();
            this.columns[p.column].add(p.node.val);
            if (p.node.left != null) {
                q.addLast(new Pair(p.node.left, p.column - 1));
            }
            if (p.node.right != null) {
                q.addLast(new Pair(p.node.right, p.column + 1));
            }
        }
    }

    public List<List<Integer>> verticalOrder(TreeNode root) {
        this.columns = new List[101];
        for (int i = 0; i < 101; i++)
            this.columns[i] = new ArrayList<>();
        bfs(root);
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < 101; i++) {
            if (this.columns[i].isEmpty())
                continue;
            result.add(this.columns[i]);
        }
        return result;
    }
}
