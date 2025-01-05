class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        store = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            store[crs].append(preq)

        res = []
        visited = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for nei in store[crs]:
                if not dfs(nei):
                    return False
            res.append(crs)
            visited.add(crs)
            cycle.remove(crs)
            return True


        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res

            

