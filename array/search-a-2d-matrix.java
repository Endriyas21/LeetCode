class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int top = 0;
        int bottom = matrix.length - 1;
        int n = matrix[0].length - 1;

        // Binary search to find the correct row
        while (top <= bottom) {
            int row = (top + bottom) / 2;
            if (target > matrix[row][n]) {
                top = row + 1;
            } else if (target < matrix[row][0]) {
                bottom = row - 1;
            } else {
                // Target is within the range of this row
                break;
            }
        }

        // If the row is not found
        if (top > bottom) {
            return false;
        }

        // Binary search within the row to find the target
        int row = (top + bottom) / 2;
        int left = 0;
        int right = n;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (matrix[row][mid] == target) {
                return true;
            } else if (matrix[row][mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }
}