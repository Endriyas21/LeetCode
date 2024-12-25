class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySeach(nums, target, findFirst):
            res = -1
            l,r = 0, len(nums)-1
            while l <=r:
                m = l + (r-l)//2
                if target < nums[m]:
                    r = m -1
                elif target > nums[m]:
                    l = m+1
                else:
                    res = m
                    if findFirst:
                        r= m-1
                    else:
                        l=m+1
            return res
        first = binarySeach(nums, target, True)
        last = binarySeach(nums, target, False)
        return [first, last]