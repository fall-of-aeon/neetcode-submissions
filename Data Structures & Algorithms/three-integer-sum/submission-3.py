class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                '''if nums[old_l] == nums[l]:
                    continue'''
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and r < len(nums) - 1 and nums[r] == nums[r+1]:   
                        r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l = l+1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r = r-1
        return result



        
        