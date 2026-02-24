void rotate(int* nums, int numsSize, int k){
    int temp[numsSize],j=0,i;
    k=k%numsSize;
    for(i=numsSize-k;i<numsSize;i++)
    {
        temp[j++]=nums[i];
    }
    for(i=0;i<numsSize-k;i++)
    {
        temp[j++]=nums[i];
    }
    for(i=0;i<numsSize;i++)
    {
        nums[i]=temp[i];
    }
}