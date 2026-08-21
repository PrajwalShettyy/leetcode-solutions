from math import gcd, lcm

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                common = 1

                for i in range(n):
                    if mask & (1 << i):
                        common = lcm(common, coins[i])

                        if common > x:
                            break

                bits = mask.bit_count()

                if bits % 2:
                    total += x // common
                else:
                    total -= x // common

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left