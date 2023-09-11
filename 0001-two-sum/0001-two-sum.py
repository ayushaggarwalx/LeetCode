class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remainder = target - nums[i]
                
            if remainder in seen:
               return [i, seen[remainder]]
            
            seen[value] = i
        