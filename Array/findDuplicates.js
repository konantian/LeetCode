/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    let result = [];
    for(let num of nums){
        if(nums[Math.abs(num)-1] < 0) result.push(Math.abs(num));
        else nums[Math.abs(num)-1] = -nums[Math.abs(num)-1];
    }
    return result;
};