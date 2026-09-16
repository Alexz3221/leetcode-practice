class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}
        for i in nums:
            freqCount[i] = freqCount.get(i, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        
        for numbers, count in freqCount.items():
            buckets[count].append(numbers)

        result = []

        for count in range(len(buckets) - 1, 0, -1):
            for numbers in buckets[count]:
                result.append(numbers)
            if (len(result) == k):
                return result
        return result