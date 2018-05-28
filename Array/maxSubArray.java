/*
#Author : Yuan Wang
#Date   : 2018-05-28

Algorithm:using dp, check previous sum, reset it to 0 if less than 0
*/

import java.lang.Math;
public class maxSubArray{
	public static void main(String[] args){
		int array[]={-2,1,-3,4,-1,2,1,-5,4};
		int sum=max_subarray(array);
		System.out.println("The largest sub array sum is: "+sum);
	}

	public static int max_subarray(int nums[]){
		int res=nums[0];
		int sum_array=nums[0];
		for(int i = 1;i<nums.length;i++){
			sum_array=Math.max(sum_array,0)+nums[i];
			res=Math.max(sum_array,res);

		}
		return res;
	}
}