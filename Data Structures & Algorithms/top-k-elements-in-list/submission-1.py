class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}
        for i in nums:
            freqCount[i] = freqCount.get(i, 0) + 1
        sortedNumbers = sorted(
            freqCount,
            key=freqCount.get,
            reverse = True
        )
        return sortedNumbers[:k]