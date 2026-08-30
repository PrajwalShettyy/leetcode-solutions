class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappearedList = []
        indexMap = { element : index for index , element in enumerate(nums)}

        for i in range(1,len(nums)+1):
            if indexMap.get(i,-1) == -1 : disappearedList.append(i)
        
        return disappearedList