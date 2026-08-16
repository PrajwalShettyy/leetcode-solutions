class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1
        leftMax , rightMax = height[left] , height[right]
        containerMax = 0
        while left < right :
            containerMax = max(containerMax,(right-left) * min(leftMax,rightMax))
            if leftMax > rightMax :
                right -= 1
                rightMax = max(rightMax,height[right])
            else :
                left += 1
                leftMax = max(leftMax,height[left])
        
        return containerMax
        