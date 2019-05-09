/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
	if(nums.length <= 1) return false;
	let buff = new Map();
	for(let i in nums){
		if(nums[i] in buff){
			return [buff[nums[i]],i];
		}
		else{
			buff[target-nums[i]] = i;
		}
	}
};
