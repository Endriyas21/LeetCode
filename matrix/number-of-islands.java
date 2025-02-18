class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0; // If the grid is empty, return 0
        }

        int numIslands = 0; // Initialize the number of islands to 0
        int rows = grid.length;
        int cols = grid[0].length;

        // Iterate through each cell in the grid
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    numIslands++; // Increment the island count
                    dfs(grid, i, j); // Perform DFS to mark all connected '1's as visited
                }
            }
        }

        return numIslands; // Return the total number of islands
    }

    // Helper function to perform DFS
    private void dfs(char[][] grid, int i, int j) {
        int rows = grid.length;
        int cols = grid[0].length;

        // Base case: if the cell is out of bounds or not '1', return
        if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] != '1') {
            return;
        }

        grid[i][j] = '0'; // Mark the cell as visited by setting it to '0'

        // Recursively visit all adjacent cells (up, down, left, right)
        dfs(grid, i - 1, j); // Up
        dfs(grid, i + 1, j); // Down
        dfs(grid, i, j - 1); // Left
        dfs(grid, i, j + 1); // Right
    }
}