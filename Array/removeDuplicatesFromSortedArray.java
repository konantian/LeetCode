/*
#Author : Yuan Wang
#Date   : 2018-05-26

Algorithm

Since the array is already sorted, we can keep two pointers ii and jj, 
where ii is the slow-runner while jj is the fast-runner. As long as 
nums[i] = nums[j]nums[i]=nums[j], we increment jj to skip the duplicate.

When we encounter nums[j] \neq nums[i]nums[j]≠nums[i], the duplicate run
has ended so we must copy its value to nums[i + 1]nums[i+1]. ii is then 
incremented and we repeat the same process again until jj reaches the end of array.

Complexity analysis

Time complextiy : O(n)O(n). Assume that nn is the length of array.
Each of ii and jj traverses at most nn steps.

Space complexity : O(1)O(1).
*/


import java.util.Arrays;

public class removeDuplicatesFromSortedArray {
    public static void main(String[] args){
        int array[] = {1,1,2,3,3,3,4,4,5};
        int count=0;
        count=removeDuplicates(array);
        System.out.println(count);
        
    }

    public static int removeDuplicates(int[] nums){
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
        }
    }
    return i + 1;
    }
}