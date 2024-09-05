class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for n in nums:
            if n in store.keys():
                return True
            else:
                store[n] = 1
        return False 