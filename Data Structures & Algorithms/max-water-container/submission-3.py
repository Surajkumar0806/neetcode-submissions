class Solution:
    def maxArea(self, heights: List[int]) -> int:
        temp = 0
        left = 0
        right = len(heights)-1
        while left < right:
            area = (right-left) * min(heights[right], heights[left])
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
            if area > temp:
                temp = area
        return temp