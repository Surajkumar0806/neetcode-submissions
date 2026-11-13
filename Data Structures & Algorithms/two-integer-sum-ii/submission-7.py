class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers)-1
        while l < r:
            nsum = numbers[r] + numbers[l]
            if nsum < target:
                l+=1
            elif nsum > target:
                r-=1
            elif nsum == target:
                return [l+1, r+1]