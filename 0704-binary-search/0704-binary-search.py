class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def BinarySearch( start , end ) :
            if start > end : return -1
            mid = (start + end) // 2
            if nums[mid] == target : return mid
            elif nums[mid] < target : return BinarySearch( mid + 1 , end )
            else : return BinarySearch( start , mid - 1 )
            
        return BinarySearch( 0 , len(nums) - 1)