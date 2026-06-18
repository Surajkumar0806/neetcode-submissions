class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        store=0
        val=[]
        freq=defaultdict(int)
        for num in nums:
            freq[num] +=1
        sorted_store=sorted(freq.items(), key=lambda x:x[1], reverse=True)
        for item in sorted_store[:k]:
            val.append(item[0])
        return val
        