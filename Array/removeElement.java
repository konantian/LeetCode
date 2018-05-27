/*Source : https://oj.leetcode.com/problems/remove-element/
Author : Yuan Wang
Date   : 2018-05-27

********************************************************************************** 
* 
* Given an array and a value, remove all instances of that value in place and return the new length.
* 
* The order of elements can be changed. It doesn't matter what you leave beyond the new length.
* 
*           
**********************************************************************************/

public class removeElement {
    public static void main(String[] args){
        int array[] = {3,2,2,3};
        int value = 3;
        int result=remove_element(array,value);

        for(int i=0;i<result;i++){
        	System.out.println(array[i]);
        }
        
    }
//Count how many elements are different with the val,and move the different elements to the front of the array
//return the count and the first count elements of the array is already been the elements that different with the
//value
    public static int remove_element(int nums[],int val){
    	int begin=0;
 		for(int i=0;i<nums.length;i++){
 			if(nums[i]!=val){
				nums[begin++]=nums[i];
			}
		}
 		return begin;  
    }
}