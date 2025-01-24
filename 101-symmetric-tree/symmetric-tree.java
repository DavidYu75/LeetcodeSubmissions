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
    public boolean isSymmetric(TreeNode root) {

        return root == null || dfs(root.left, root.right);
    }

    private boolean dfs(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }
        if (left == null || right == null) {
            return false;
        }
        if (left == null || right == null) {
            return false;
        }

        return left.val == right.val
            && dfs(left.right, right.left)
            && dfs(left.left, right.right);
    }
}

public class FloodFill {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int originalColor = image[sr][sc];
        
        // If the original color is the same as the new color, no need to change anything
        if (originalColor != newColor) {
            dfs(image, sr, sc, originalColor, newColor);
        }
        
        return image;
    }

    private void dfs(int[][] image, int row, int col, int originalColor, int newColor) {
        // Check if the current cell is out of bounds or not the original color
        if (row < 0 || row >= image.length || col < 0 || col >= image[0].length || image[row][col] != originalColor) {
            return;
        }

        // Change the color of the current cell
        image[row][col] = newColor;

        // Recursively call the DFS function for all four directions
        dfs(image, row + 1, col, originalColor, newColor); // Down
        dfs(image, row - 1, col, originalColor, newColor); // Up
        dfs(image, row, col + 1, originalColor, newColor); // Right
        dfs(image, row, col - 1, originalColor, newColor); // Left
    }
}