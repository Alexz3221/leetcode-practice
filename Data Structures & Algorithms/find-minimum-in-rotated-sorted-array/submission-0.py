class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
  
        while left < right:
            mid = (left + right) // 2
  
            if nums[mid] > nums[right]:
                # Minimum must be strictly to the right of mid.
                left = mid + 1
            else:
                # Mid might be the minimum, or the minimum is to its left.
                right = mid
  
        return nums[left]
