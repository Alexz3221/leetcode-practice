class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = [False] * (len(nums) + 1)
        for i in nums:
            if 0 < i <= len(nums):
                seen[i] = True
        print(seen)
        for i in range(1, len(nums) + 1):
            
            if not seen[i]:
                return i
        return len(nums) + 1