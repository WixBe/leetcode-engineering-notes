import array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        tmp=array.array('i')
        if k!=0:
            for i in range(len(nums)-k, len(nums)):
                tmp.append(nums[i])
            for i in range(len(nums)-k):
                tmp.append(nums[i])
            for i in range(len(nums)):
                nums[i]=tmp[i]