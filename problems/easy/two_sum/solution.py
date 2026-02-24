class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        n = len(nums)

        for i in range(n):
            nmap[nums[i]] = i
        
        for i in range(n):
            complement = target - nums[i]
            if complement in nmap and nmap[complement] != i:
                return [i, nmap[complement]]
        
        return []