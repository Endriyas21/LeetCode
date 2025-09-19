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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        queue<TreeNode*> q;
        if(!root) return res;
        q.push(root);
        
        while(!q.empty()){
            int level_size = q.size();
            vector<int> temp_store;
            for(int i=0; i < level_size; i++){
                TreeNode* node = q.front();
                q.pop();
                if(node){
                    temp_store.push_back(node->val);
                    q.push(node->left);
                    q.push(node->right);
                }                 
            }
        if(!temp_store.empty()){
            res.push_back(temp_store);
        }              
        }
        return res;
    }
};