class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            
            if i>0 and nums[i-1] == nums[i]:
                continue
            nums1 = nums[i]
            l,r = i+1, len(nums)-1
            while l < r:
                total = nums1 + nums[l] + nums[r]
                if total >0:
                    r-=1
                if total <0:
                    l+=1
                if total == 0:
                    res.append([nums1, nums[l], nums[r]])
                    l+=1
                while l<r and nums[l-1] == nums[l]:
                    l+=1
        return res
