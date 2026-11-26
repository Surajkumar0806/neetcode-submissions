class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = high
        while low <= high:
            mid = (low + high)//2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(float(pile) / mid)
            if total_hours <= h:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result 

# here low, high and middle are not about index they are about the values 
# pile / k is something like distance / speed where pile is the current distance need to be covered at the rate of k which gives how much time does it take 
