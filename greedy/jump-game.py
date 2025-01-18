class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for i in range(len(nums)):
            curr = i + nums[i]
            if curr == len(nums)-1:
                return True
        #print(curr)
        return curr == len(nums)-1