class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, i+k+1):
                if j == length:
                    break
                if nums[i] == nums[j]:
                    return True
        return False

        