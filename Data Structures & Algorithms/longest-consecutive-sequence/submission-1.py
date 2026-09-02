class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_count = 0
        for num in nums:
            count = 0
            if num-1 not in seen:
                while num + count in seen:
                    count +=1
            elif num+1 in seen:
                continue
            max_count = max(max_count, count)

        return max_count
            
        