class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        for i in range(len(nums) - 2 , -1 , -2) :
            maxSum += nums[i]
        
        return maxSum

        