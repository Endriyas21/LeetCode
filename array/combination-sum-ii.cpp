class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());  // ✅ must sort for deduplication
        vector<vector<int>> res;
        vector<int> subarray;
        dfs(0, 0, candidates, target, subarray, res);
        return res;
    }

private:
    void dfs(int start, int _sum, const vector<int>& candidates, int target,
             vector<int>& subarray, vector<vector<int>>& res) {
        if (_sum == target) {
            res.push_back(subarray);
            return;
        }
        if (_sum > target) return;

        for (int i = start; i < candidates.size(); ++i) {
            // ✅ skip duplicates at the same recursion level
            if (i > start && candidates[i] == candidates[i - 1]) continue;

            // ✅ include candidates[i]
            subarray.push_back(candidates[i]);

            // ✅ move to next index (each element can be used at most once)
            dfs(i + 1, _sum + candidates[i], candidates, target, subarray, res);

            // ✅ backtrack
            subarray.pop_back();
        }
    }
};