class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seatMap = {
            f"{row}-{seat}": True for row, seat in reservedSeats
        }

        count = 2 * n

        def isSafe(row, seats):
            for seat in seats:
                if seatMap.get(f"{row}-{seat}", False):
                    return 0
            return 1

        rows = set(row for row, seat in reservedSeats)

        for row in rows:
            left = isSafe(row, range(2, 6))   # 2-5
            middle = isSafe(row, range(4, 8)) # 4-7
            right = isSafe(row, range(6, 10)) # 6-9

            if left and right:
                count += 0       # already counted 2
            elif left or middle or right:
                count -= 1        # only 1 family instead of 2
            else:
                count -= 2        # no family

        return count