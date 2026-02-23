namespace BruteForce {
    function twoSum(nums: number[], target: number): number[] {
        for(let i=0; i<nums.length; i++){
            for(let j=i+1; j<nums.length; j++) {
                if (nums[i] + nums[j] == target){
                    return [i, j]
                }
            }
        }
        return [];
    }

    // Example usage:
    const nums = [3, 2, 4];
    const target = 6;
    const result = twoSum(nums, target);
    console.log(result); // Output: [1, 2]
}