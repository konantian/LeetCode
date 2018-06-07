import java.util.*;

public class moveZeros{
	public static void main(String[] args){
		int array[]={0,1,0,3,12};
		move_zeros(array);
		System.out.println(Arrays.toString(array));
	}

	public static void move_zeros(int[] nums) {
        int nonZeroIndex = 0;
        int ptrIndex = 0;
        while (ptrIndex < nums.length) {
            if (nums[ptrIndex] == 0) {
                ptrIndex++;
            } else {
                int tmp = nums[ptrIndex];
                nums[ptrIndex] = nums[nonZeroIndex];
                nums[nonZeroIndex] = tmp;
                nonZeroIndex++;
                ptrIndex++;
            }
        }
    }
}