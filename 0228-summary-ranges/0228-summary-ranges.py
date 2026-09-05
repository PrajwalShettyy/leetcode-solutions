class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        summaryRangeList = []
        i , j , diff = 0 , 0 , 0
        
        while i < len(nums) :
            while j < len(nums) and  ( nums[i] + diff ) == nums[j] :
                j , diff = j + 1 , diff + 1
            summaryRangeList.append(f"{nums[i]}->{nums[j - 1]}" if i !=( j - 1) else f"{nums[i]}")
            i , diff = j , 0

        return summaryRangeList