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
    public boolean isBalanced(TreeNode root) {
        return checkHeight(root).isBalanced;
    }

    // Helper class to store height and balance status
    private static class HeightBalance {
        int height;
        boolean isBalanced;

        HeightBalance(int height, boolean isBalanced) {
            this.height = height;
            this.isBalanced = isBalanced;
        }
    }

    // Helper function to check the height and balance of the tree
    private HeightBalance checkHeight(TreeNode node) {
        if (node == null) {
            return new HeightBalance(0, true); // Base case: if the node is null, return height 0 and balanced true
        }

        HeightBalance left = checkHeight(node.left); // Recursively find the height and balance of the left subtree
        HeightBalance right = checkHeight(node.right); // Recursively find the height and balance of the right subtree

        // Calculate the height of the current node as the max height of its subtrees plus one
        int currentHeight = 1 + Math.max(left.height, right.height);

        // Determine if the current node is balanced
        boolean isBalanced = left.isBalanced && right.isBalanced && Math.abs(left.height - right.height) <= 1;

        return new HeightBalance(currentHeight, isBalanced);
    }
}