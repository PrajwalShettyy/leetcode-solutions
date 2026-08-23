class Solution:
    def sumGame(self, num: str) -> bool:

        def calculate(num: str) -> tuple[int, int, int, int]:
            left , left_q , right , right_q = 0 , 0 , 0 , 0
            mid = len(num) // 2

            for index, char in enumerate(num):
                if index < mid:
                    if char == '?': left_q += 1
                    else: left += int(char)
                else:
                    if char == '?': right_q += 1
                    else: right += int(char)

            return left, right, left_q, right_q

        left, right, left_q, right_q = calculate(num)

        diff = left - right

        return True if (left_q + right_q) % 2 == 1 else   diff != 9 * (right_q - left_q) // 2   