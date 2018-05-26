/*
#Author : Yuan Wang
#Date   : 2018-05-26

Algorithm:

The brute force approach is simple. Loop through each element x
and find if there is another value that their sum is target

Complexity Analysis

Time complexity : O(n^2)
​For each element, we try to find its complement by looping through the 
rest of array which takes O(n)O(n) time. Therefore, the time complexity is O(n^2)

Space complexity : O(1)
*/

import java.util.Arrays;
public class TwoSum {
    public static void main(String[] args){
        int array[] = {2,7,11,15};
        int target = 9;
        int index[]=twosum(array,target);
        System.out.println(Arrays.toString(index));
        
    }

    public static int[] twosum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[j] == target - nums[i]) {
                return new int[] { i, j };
            }
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}
}
