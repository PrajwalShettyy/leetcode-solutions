class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefixSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefixSum += nums[i]
            else:
                break

        while prefixSum in nums:
            prefixSum += 1

        return prefixSum