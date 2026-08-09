class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache 
        def minmaxDP(position,M) :
            return 0 if position >= len(piles) else max ( sum(piles[position : ]) - minmaxDP(position + i , max(i ,M)) for i in range(1 , 2 * M + 1))
        
        return minmaxDP(0,1)

