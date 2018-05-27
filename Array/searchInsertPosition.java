/*
Source : https://oj.leetcode.com/problems/search-insert-position/
Inspired by : http://www.jiuzhang.com/solutions/search-insert-position/
Author : Yuan Wang
Date   : 2018-05-27
*/

import java.util.Arrays;

public class searchInsertPosition{
	public static void main(String[] args){
		int array[] = {1,3,5,6};
		int target=2;
		int index=search_insert(array,target);
		System.out.println(index);
	}

	public static int search_insert(int nums[],int target){
		int low=0;
		int high=nums.length-1;
		while(high>=low){
			int middle=(low+high)/2;
			if(nums[middle]==target){
				return middle;
			}

			else if(nums[middle] < target){
				low=middle+1;
			}

			else high=middle-1;
		}

		return low;
	}
}