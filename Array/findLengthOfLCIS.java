import java.util.*;

public class findLengthOfLCIS{
	public static void main(String[] args){
		int array[]={1,3,5,4,7};
		int number=find_length(array);
		System.out.println(number);
	}

	public static int find_length(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int count = 1;
        int res = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                count++;
                res = Math.max(count, res);
            } else count = 1;
        }
        return res;
    }
}