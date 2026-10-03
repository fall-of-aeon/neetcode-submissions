class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set_of_arr = set()
        for i in range(len(nums)):
            if nums[i] in set_of_arr:
                    return True
            else:
                set_of_arr.add(nums[i])
                if(len(set_of_arr) > k):
                    set_of_arr.remove(nums[i-k])
        return False

        