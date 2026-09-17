class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxFound = -1
        i = 0
        j = len(heights) -1 
        while i < j:
            current = min(heights[i], heights[j]) * (j - i)
            if current > maxFound:
                maxFound = current
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            else:
                i += 1
        return maxFound