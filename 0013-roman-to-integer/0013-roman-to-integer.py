class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = { 'I' : 1 , 'V' : 5 , 'X' : 10 , 'L' : 50 , 'C' : 100 , 'D' : 500 , 'M' : 1000 }
        intNum , prevNum = 0 , 0

        for rNum in s :
            intNum = ( intNum + romanMap[rNum] ) if prevNum >= romanMap[rNum] else ( intNum + romanMap[rNum] - ( 2 * prevNum ) )
            prevNum = romanMap[rNum]
        return intNum