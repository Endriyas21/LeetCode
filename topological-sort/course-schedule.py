class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        store = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            store[crs].append(preq)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if store[crs] == []:
                return True
            visited.add(crs)
            for preq in store[crs]:
                if not dfs(preq): return False
            store[crs] = []
            visited.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
