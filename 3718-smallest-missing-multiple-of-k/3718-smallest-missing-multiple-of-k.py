class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiples , i = k , 1
        for e in sorted(nums) :
            if e == (multiples * i):
                i += 1
            elif e > (multiples * i) :
                return (multiples * i)
        
        return multiples * (i)