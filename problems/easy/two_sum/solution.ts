function twoSum(nums: number[], target: number): number[] {
    const nmap = new Map<number, number>();
    const n = nums.length;

    for(let i=0; i<n; i++){
        nmap.set(nums[i], i);
    }

    for(let i=0; i<n; i++){
        const complement = target - nums[i];
        if(nmap.has(complement) && nmap.get(complement) !== i){
            return [i, nmap.get(complement)]
        }
    }

    return []
};