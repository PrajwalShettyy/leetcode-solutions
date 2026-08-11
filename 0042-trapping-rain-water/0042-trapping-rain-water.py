class Solution:
    def trap(self, height: List[int]) -> int:
        
        def trapped( left, leftMax , right ,rightMax , water ) :
            if left > right : return water
            if height[leftMax] >= height[rightMax] :
                rightMax = right if height[right] > height[rightMax] else rightMax
                return trapped(left ,leftMax , right - 1 , rightMax , water + (height[rightMax] - height[right]) ) 
            else :
                leftMax = left if height[left] > height[leftMax] else leftMax
                return trapped(left + 1,leftMax , right , rightMax , water + (height[leftMax] - height[left]) ) 
            
        return trapped(1,0 , len(height) - 2 , len(height) - 1 , 0 ) 