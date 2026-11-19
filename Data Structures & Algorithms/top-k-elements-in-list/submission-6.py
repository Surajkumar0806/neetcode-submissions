class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        val = []
        for i in nums:
            freq[i]+=1
        sorted_key = sorted(freq.items(), key = lambda x : x[1], reverse = True)
        for item in sorted_key[:k]:
            val.append(item[0])
        return val
            