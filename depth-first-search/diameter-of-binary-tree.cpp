/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        vector<int> res(1, 0);
        dfs(root, res);
        return res[0];

    }
public:
    int dfs(TreeNode* node, vector<int>& res){
        if(!node) return 0;
        int left = dfs(node->left, res);
        int right = dfs(node->right, res);
        
        res[0] = max(res[0], left+right);
        return 1 + max(left, right);

    }
};