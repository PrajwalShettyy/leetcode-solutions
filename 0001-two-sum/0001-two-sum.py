class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for index , element in enumerate(nums):
            if  seenMap.get(target - element , -1 ) != -1 :
                return [seenMap[target - element] , index]
            seenMap[element] = index