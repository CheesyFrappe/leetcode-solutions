class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        freq_list = [v for k,v in d.items()]
        return max(freq_list) * freq_list.count(max(freq_list)) 
