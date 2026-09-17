class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thing = {}
        for i in range(len(nums)):
            otherThing = target - nums[i]
            if otherThing in thing:
                return [thing[otherThing], i]
            thing[nums[i]] = i
        return []