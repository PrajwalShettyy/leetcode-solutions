class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:

        i = 2
        arr1 , arr2 = [nums[0]],[nums[1]]

        for i in range(2,len(nums)) :
            if arr1[~0] > arr2[~0] : arr1.append(nums[i])
            else : arr2.append(nums[i])
        
        return arr1 + arr2