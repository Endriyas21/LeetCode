class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        store = collections.defaultdict(int)
        l,total, res = 0, 0, 0
        
        for r in range(len(fruits)):
            store[fruits[r]]+=1
            total+=1
            while len(store) > 2:
                f = fruits[l]
                store[f] -=1
                total -=1
                l+=1
                if not store[f]:
                    store.pop(f)
            res = max(res, total)
        return res