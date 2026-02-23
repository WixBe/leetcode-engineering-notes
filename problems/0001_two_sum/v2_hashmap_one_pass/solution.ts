namespace HashMap {
    function twoSum(nums: number[], target: number): number[] {
        const nmap = new Map<number, number>();
        const n = nums.length;

        for (let i = 0; i < n; i++) {
            nmap.set(nums[i], i);
        }

        for (let i = 0; i < n; i++) {
            const complement = target - nums[i];
            if (nmap.has(complement) && nmap.get(complement)! !== i) {
                return [i, nmap.get(complement)!];
            }
        }

        return [];
    }

    // Example usage:
    const testNums = [3, 2, 4];
    const testTarget = 6;
    const result = twoSum(testNums, testTarget);
    console.log(result); // Output: [1, 2]
}