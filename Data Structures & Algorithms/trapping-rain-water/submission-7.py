class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        left_max_array = []
        right_max_array = []
        left_max = right_max = 0 
        for i in range(n):
            left_max = max(left_max, height[i])
            left_max_array.append(left_max)
        for i in range(n-1, -1, -1):
            right_max = max(right_max, height[i])
            right_max_array.append(right_max)
        right_max_array.reverse()
        for i in range(n):
            water+= min(left_max_array[i], right_max_array[i]) - height[i]
        return water 