class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        mc=0
        mel=0
        el=nums[0]
        for i in range(len(nums)):
            if el==nums[i]:
                c+=1
                if c>mc:
                    mc=c
                    mel=el
            else:
                c=1
                el=nums[i]
        return mel