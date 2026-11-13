class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n -1
        left_max=right_max = water = 0
        left_max_array = []
        right_max_array = []
        for i in height:
            left_max = max(left_max, i)
            left_max_array.append(left_max)
        for i in height[::-1]:
            right_max = max(right_max, i)
            right_max_array.append(right_max)
        right_max_array.reverse()
        for i in range(n):
            water+= min(left_max_array[i], right_max_array[i]) - height[i]
        return water 