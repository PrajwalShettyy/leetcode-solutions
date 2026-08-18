class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}

        for i in range(len(nums) - k + 1):
            window = set(nums[i:i+k])

            for num in window:
                count[num] = count.get(num, 0) + 1

        ans = -1

        for num, occurrences in count.items():
            if occurrences == 1:
                ans = max(ans, num)

        return ans