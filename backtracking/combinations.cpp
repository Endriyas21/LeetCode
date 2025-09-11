class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> candidates;
        for (int i = 1; i <= n; i++) {
            candidates.push_back(i);
        }

        vector<int> subarray;
        dfs(0, k, subarray, res, candidates);
        return res;
    }

private:
    void dfs(int i, int k, vector<int>& subarray, vector<vector<int>>& res, vector<int>& candidates) {
        if (subarray.size() == k) {
            res.push_back(subarray);
            return;
        }

        if (i >= candidates.size()) return;

        // include candidates[i]
        subarray.push_back(candidates[i]);
        dfs(i + 1, k, subarray, res, candidates);

        // exclude candidates[i]
        subarray.pop_back();
        dfs(i + 1, k, subarray, res, candidates);
    }
};