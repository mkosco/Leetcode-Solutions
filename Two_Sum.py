class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in checked:
                return [checked[complement], i]
            else:
                checked[nums[i]] = i
        