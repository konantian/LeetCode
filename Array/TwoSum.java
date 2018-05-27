/*
#Author : Yuan Wang
#Date   : 2018-05-26

Algorithm:

The brute force approach is simple. Loop through each element x
and find if there is another value that their sum is target

Complexity Analysis:

Time complexity : O(n). We traverse the list containing nn elements 
exactly twice. Since the hash table reduces the look up time to O(1), 
the time complexity is O(n).

Space complexity : O(n). The extra space required depends on the 
number of items stored in the hash table, which stores exactly nn elements.
*/
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;
public class TwoSum {
    public static void main(String[] args){
        int array[] = {2,7,11,15};
        int target = 9;
        int index[]=twoSum(array,target);
        System.out.println(Arrays.toString(index));
        
    }

    public static int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], i);
    }
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement) && map.get(complement) != i) {
            return new int[] { i, map.get(complement) };
        }
    }
    throw new IllegalArgumentException("No two sum solution");
    }
}
