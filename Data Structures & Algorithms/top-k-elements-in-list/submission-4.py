class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1) ]

        final  = [];
        for number, freq in count.items():
            buckets[freq].append(number)
        for i in range(len(buckets) - 1, 0, -1):
            for numb in buckets[i]:
                final.append(numb)
                if(len(final) == k):
                    return final
        return []
        """
        sortCount = sorted(count, key = count.get, reverse = True)
        final = []
        for i in range(0, k):
            final.append(sortCount[i])
        return final
        """