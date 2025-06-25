// Last updated: 6/25/2025, 11:42:47 AM
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    for (i = 1; i < nums.length;i++){
        nums[i]= nums[i-1] + nums[i]
    }
    return nums
};