class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squareList = [ i * i for i in range(1,int(n**0.5)+1)]
        @cache
        def move(stoneCount):
            return 0 if not stoneCount else max( 1 - move(stoneCount - square) for square in squareList if square <= stoneCount )
        return move(n) == 1

            
        