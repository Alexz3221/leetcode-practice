class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        newNums = sorted(nums)
        print (newNums)
        i = 0
        k = 0
        for j in newNums:
            if i == 0:
                k = k + j
                i = 1
            elif i == 1:
                k = k - j
                i = 0

        return k