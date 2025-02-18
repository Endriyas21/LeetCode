class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // Build the graph
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] prerequisite : prerequisites) {
            graph.get(prerequisite[1]).add(prerequisite[0]);
        }

        // Array to track the state of each node (0 = unvisited, 1 = visiting, 2 = visited)
        int[] visited = new int[numCourses];

        // Perform DFS for each course
        for (int i = 0; i < numCourses; i++) {
            if (visited[i] == 0) {
                if (hasCycle(graph, visited, i)) {
                    return false; // If a cycle is detected, return false
                }
            }
        }

        return true; // If no cycles are detected, return true
    }

    // Helper function to perform DFS and detect cycles
    private boolean hasCycle(List<List<Integer>> graph, int[] visited, int course) {
        if (visited[course] == 1) {
            return true; // A cycle is detected
        }
        if (visited[course] == 2) {
            return false; // The node has already been visited and no cycle was found
        }

        visited[course] = 1; // Mark the node as visiting

        // Visit all the neighbors
        for (int neighbor : graph.get(course)) {
            if (hasCycle(graph, visited, neighbor)) {
                return true; // If a cycle is detected in any neighbor, return true
            }
        }

        visited[course] = 2; // Mark the node as visited
        return false; // No cycle detected
    }
}