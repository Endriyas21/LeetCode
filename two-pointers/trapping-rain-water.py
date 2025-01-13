class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        leftmax = [0]*n
        leftmax[0] = height[0]
        for i in range(1,n):
            leftmax[i] = max(height[i], leftmax[i-1])
        rightmax = [0]*n
        rightmax[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            rightmax[i] = max(height[i], rightmax[i+1])
        res = 0
        for i in range(len(height)):
            res += min(leftmax[i], rightmax[i]) - height[i]
        return res
