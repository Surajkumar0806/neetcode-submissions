class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            sorted_key = "".join(sorted(word))
            seen[sorted_key].append(word)
        return list(seen.values())
