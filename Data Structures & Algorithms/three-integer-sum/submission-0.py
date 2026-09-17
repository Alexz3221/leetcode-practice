class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sNums = sorted(nums)
        for k in range(len(nums) - 2):
            if k > 0 and sNums[k] == sNums[k - 1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                total = sNums[k] + sNums[i] + sNums[j]
                if total == 0:
                    result.append([sNums[k],sNums[i],sNums[j]])
                    j -= 1
                    i += 1
                    while i < j and sNums[i] == sNums[i - 1]:
                        i += 1
                    while i < j and sNums[j] == sNums[j + 1]:
                        j -= 1

                elif total > 0:
                    j -= 1
                elif total < 0:
                    i += 1
        return result