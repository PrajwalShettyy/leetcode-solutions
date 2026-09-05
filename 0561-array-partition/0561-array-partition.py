class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum( nums[i] for i in range(len(nums) - 2 , -1 , -2 ))