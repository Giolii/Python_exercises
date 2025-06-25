// Last updated: 6/25/2025, 11:42:48 AM
/**
 * @param {number} num
 * @return {number}
 */

 function helper(num,steps){
    if(num === 0) return steps
    if(num%2 === 0) return helper(num/2,steps+1)
    return helper(num-1,steps+1)
}

var numberOfSteps = function(num) {
    return helper(num,0)
};

