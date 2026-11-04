class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        l, r = 0, len(heights) - 1

        while (l < r):

            width = r - l
            height = min(heights[l], heights[r])

            max_water = max(width * height, max_water)

            if heights[l] == height:
                l += 1
            else:
                r -= 1

        return max_water

            