class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=set()
        for i in range(len(nums)):
            needed = target-nums[i]
            if needed in seen:
                index1=nums.index(needed) 
                return [index1, i]
            seen.add(nums[i])
            
