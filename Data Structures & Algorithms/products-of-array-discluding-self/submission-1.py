class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mul, r_mul = 1, 1
        n = len(nums)
        r_arr = n * [0]
        l_arr = n * [0]
        res = n * [0]
        for i in range(n):
            j = -i - 1
            l_arr[i] = l_mul
            r_arr[j] = r_mul
            l_mul *= nums[i]
            r_mul *= nums[j]
        for i in range(n):
            res[i] = r_arr[i] * l_arr[i]
        return res
