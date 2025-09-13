class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        store = {n:0 for n in nums}
        for n in nums:
            store[n]+=1
        res = []
        def dfs():
            if len(res) == len(nums):
                ans.append(res.copy())
            for n in store:
                if store[n] > 0:
                    res.append(n)
                    store[n] -=1
                    
                    dfs()
                    store[n]+=1
                    res.pop()
        dfs()
        return ans