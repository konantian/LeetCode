/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let result = [];
    let i = 0;
    let j = 0;
    while(i < nums1.length & j < nums2.length){
        if(nums1[i] <= nums2[j]){
            result.push(nums1[i]);
            i++;
        }else{
            result.push(nums2[j]);
            j++;
        }
    }
    for(;i<nums1.length;i++) result.push(nums1[i]);
    for(;j<nums2.length;j++) result.push(nums2[j]);
    if(result.length % 2 == 0){
        return (result[result.length/2]+result[result.length/2-1])/2;
    }
    return result[Math.floor(result.length/2)];
    
};