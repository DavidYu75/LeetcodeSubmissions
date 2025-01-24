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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        dfs(output, root, 0);
        return output;
    }

    private void dfs(List<List<Integer>> output, TreeNode root, int height) {
        if (root == null) {
            return;
        }

        if (height >= output.size()) {
            output.add(new LinkedList<Integer>());
        }

        output.get(height).add(root.val);
        dfs(output, root.left, height + 1);
        dfs(output, root.right, height + 1);
    }
}