class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        totalXOR = 0
        for x in nums: totalXOR ^= x
        return len(nums) if totalXOR != 0 else len(nums) - 1 if any(nums) else 0