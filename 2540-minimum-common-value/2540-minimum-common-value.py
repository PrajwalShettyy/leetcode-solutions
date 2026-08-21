class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        numMap = {num : True for num in nums1 }
        minValue = float('inf')
        for e in nums2 :
            if numMap.get(e,False) and minValue > e : minValue = e
        return minValue if minValue < float('inf') else -1