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
            for nei in store[crs]:
                if not dfs(nei): return False
            store[crs] = []
            visited.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True 
        # visited = set()
        # completed = set()
        
        # def dfs(crs):
        #     if crs in visited:
        #         return False
        #     if crs in completed:
        #         return True
            
        #     visited.add(crs)
        #     for nei in store[crs]:
        #         if not dfs(nei):
        #             return False
        #     visited.remove(crs)
        #     completed.add(crs)
        #     return True

        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True
