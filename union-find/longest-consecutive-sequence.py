class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for n in nums:
            count = 0
            if (n-1) not in store:
                count=0
                while (n+count) in store:
                    count+=1
                res = max(res, count)
        return res
