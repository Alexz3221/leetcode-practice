class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[len(piles) - 1]
        while left < right:
            speed = (left + right) // 2
            hours = 0
            for i in piles:
                pileHour = (i + speed - 1) // speed
                hours += pileHour
            if(hours > h):
                left = speed + 1
            else:
                right = speed

        return left