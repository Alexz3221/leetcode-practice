class Solution:
    def climbStairs(self, n: int) -> int:
        ways_zero = 1
        ways_one = 1

        for stairs in range(2, n + 1):
            current = ways_one + ways_zero
            ways_zero = ways_one
            ways_one = current

        return ways_one