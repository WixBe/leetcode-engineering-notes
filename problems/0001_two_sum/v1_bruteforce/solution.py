from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(nums[i], nums[j])
                if nums[i] + nums[j] == target:
                    result = [i, j]
        return result
    
# Example usage:
nums = [3,2,4]
target = 6
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]