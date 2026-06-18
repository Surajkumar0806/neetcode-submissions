class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=set()
        for i in range(len(nums)):
            needed = target-nums[i]
            if needed in seen:
                index1=nums.index(needed) 
                index2=i
                return [index1, index2]
            seen.add(nums[i])
            
