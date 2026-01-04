/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    private void dfs(TreeNode node, StringBuilder sb) {
        if (node == null){
            sb.append("null");
            sb.append(",");
            return;
        }
        sb.append(Integer.toString(node.val));
        sb.append(",");
        dfs(node.left, sb);
        dfs(node.right, sb);
    }
    
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        dfs(root, sb);
        return sb.toString();
    }

    private int i;

    private TreeNode decode(String[] data) {
        int n = data.length;
        if (i >= n) 
            return null;
        if ("null".equals(data[i])) {
            this.i++;
            return null;
        }
        TreeNode node = new TreeNode();
        node.val = Integer.parseInt(data[i]);
        this.i++; // Go deeper in the interations
        node.left = decode(data);
        node.right = decode(data);
        return node;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] parts = data.split(",");
        this.i = 0;
        TreeNode root = decode(parts);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
