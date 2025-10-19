class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
         if (mat.empty() || mat[0].empty())
            return {};

        int rows = mat.size();
        int cols = mat[0].size();
        vector<int> res;
        res.reserve(rows * cols);  // Pre-allocate for performance

        int r = 0, c = 0;
        bool up = true;

        for (int i = 0; i < rows * cols; ++i) {
            res.push_back(mat[r][c]);

            if (up) {
                if (c == cols - 1) {
                    ++r;
                    up = false;
                } else if (r == 0) {
                    ++c;
                    up = false;
                } else {
                    --r;
                    ++c;
                }
            } else {
                if (r == rows - 1) {
                    ++c;
                    up = true;
                } else if (c == 0) {
                    ++r;
                    up = true;
                } else {
                    ++r;
                    --c;
                }
            }
        }

        return res;
    }
};