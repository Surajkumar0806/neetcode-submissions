class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left_max=0
        left_max_array=[]
        right_max=height[n-1]
        right_max_array=[]
        water=0
        for num in height:
            left_max=max(left_max, num)
            left_max_array.append(left_max)
        for num in height[::-1]:
            right_max=max(right_max,num)
            right_max_array.append(right_max)
        right_max_array.reverse()
        for i in range(n):
            water +=min(left_max_array[i], right_max_array[i])- height[i]

        return water