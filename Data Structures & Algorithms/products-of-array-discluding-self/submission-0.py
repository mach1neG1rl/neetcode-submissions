class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left = 1
        
        for i in range(1, len(nums)):        
            left *= nums[i-1]
            res[i] *= left

        right = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
            
        return res