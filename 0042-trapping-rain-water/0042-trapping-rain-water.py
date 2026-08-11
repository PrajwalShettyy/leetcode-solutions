class Solution:
    def trap(self, height: List[int]) -> int:
        left , leftMax = 1 , height[0]
        right , rightMax = len(height) - 2 , height[len(height) - 1]
        water = 0

        while left <= right :
            if leftMax >= rightMax :
                rightMax = max(rightMax,height[right])
                water += (rightMax - height[right])
                right -= 1
            else :
                leftMax = max(leftMax,height[left])
                water += (leftMax - height[left])
                left += 1
        return water