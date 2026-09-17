class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        sortCount = sorted(count, key = count.get, reverse = True)
        final = []
        for i in range(0, k):
            final.append(sortCount[i])
        return final