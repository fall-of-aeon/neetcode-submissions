from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = 0
        max_key = 0
        for i in freq:
            if freq[i] > max_freq:
                max_freq = freq[i]
                max_key = i
        return max_key
            
