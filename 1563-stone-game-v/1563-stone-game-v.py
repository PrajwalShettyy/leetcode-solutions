from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for idx in range(n):
            prefix[idx + 1] = prefix[idx] + stoneValue[idx]

        NEG = float('-inf')
        dp = [[0] * n for _ in range(n)]

        # left-scan state (per row i): mid[i] tracks split point, leftMax[i] running max
        mid = [i - 1 for i in range(n)]
        leftMax = [NEG] * n

        # right-scan state (per col j): kmin[j] tracks split point, rightMax[j] running max
        kmin = [j for j in range(n)]
        rightMax = [NEG] * n

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                S = prefix[j + 1] - prefix[i]

                # advance left pointer for row i
                while mid[i] + 1 <= j - 1 and 2 * (prefix[mid[i] + 2] - prefix[i]) <= S:
                    mid[i] += 1
                    cand = (prefix[mid[i] + 1] - prefix[i]) + dp[i][mid[i]]
                    if cand > leftMax[i]:
                        leftMax[i] = cand

                # advance right pointer for col j
                while kmin[j] - 1 >= i and 2 * (prefix[j + 1] - prefix[kmin[j]]) <= S:
                    kmin[j] -= 1
                    cand = (prefix[j + 1] - prefix[kmin[j] + 1]) + dp[kmin[j] + 1][j]
                    if cand > rightMax[j]:
                        rightMax[j] = cand

                best = NEG
                if leftMax[i] > best:
                    best = leftMax[i]
                if rightMax[j] > best:
                    best = rightMax[j]
                dp[i][j] = best

        return dp[0][n - 1]