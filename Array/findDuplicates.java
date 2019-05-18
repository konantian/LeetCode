import java.util.*;

public class findDuplicates{
	public static void main(String args[]){
		int nums[] = {4,3,2,7,8,2,3,1};
		System.out.println(FindDuplicates(nums));

	}

	public static List<Integer> FindDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<>();
        for(int num:nums){
            if(nums[Math.abs(num)-1] < 0) result.add(Math.abs(num));
            else nums[Math.abs(num)-1] *= -1;
        }
        return result;
    }
}