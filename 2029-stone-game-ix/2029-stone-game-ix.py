class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        def check(cnt):
            if cnt[1] == 0:
                return False

            cnt[1] -= 1

            length = 1 + min(cnt[1], cnt[2]) * 2 + cnt[0]

            if cnt[1] > cnt[2]:
                cnt[1] -= 1
                length += 1

            return length % 2 == 1 and cnt[1] != cnt[2]

        return check(cnt[:]) or check([cnt[0], cnt[2], cnt[1]])