class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
            
        sorted_ks = sorted(frequencies, key=lambda x : frequencies[x], reverse=True)
        return sorted_ks[:k]


