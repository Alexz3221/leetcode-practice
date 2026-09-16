class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        eMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in eMap:
                return [eMap[diff], i]
            else:
                eMap[nums[i]] = i