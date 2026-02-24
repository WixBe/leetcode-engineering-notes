int removeElement(int* nums, int numsSize, int val){
    int i=0,k=0,j,temp[10*(int)malloc(sizeof(int))];
    j=numsSize;
   for(i=0;i<numsSize;i++)
   {
       if(nums[i]==val)
       {
           j--;
       }
       else
       {
           temp[k++]=nums[i];
       }
   }
   for(i=0;i<k;i++)
   {
       nums[i]=temp[i];
   }
   return j;
}