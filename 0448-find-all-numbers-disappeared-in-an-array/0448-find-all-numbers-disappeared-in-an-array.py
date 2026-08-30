class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        indexMap = { element : index for index , element in enumerate(nums)}
        return [ element for element in range(1,len(nums) + 1) if indexMap.get(element,-1) == -1 ]