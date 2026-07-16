class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, n in enumerate(nums):
            res = target - n
            if res in dic:
                return [dic[res], i]
            dic[n] = i
        
