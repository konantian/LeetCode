import java.util.*;

public class findDisappearedNumbers{
	public static void main(String[] args){
		int nums[]={4,3,2,7,8,2,3,1};
		List<Integer> list = find_numbersB(nums);
		System.out.println(list);
	}

	public static List<Integer> find_numbers(int nums[]){
		Set<Integer> nums_set = new HashSet<Integer>();
		Set<Integer> all_nums = new HashSet<Integer>();
		List<Integer> list= new ArrayList<>();
		for(int x:nums) nums_set.add(x);
		for(int i=1;i<nums.length+1;i++) all_nums.add(i);

		all_nums.removeAll(nums_set);
		for(int n:all_nums) list.add(n);

		return list;
	}

	public static List<Integer> find_numbersB(int nums[]){
		List<Integer> ret = new ArrayList<Integer>();
        
        for(int i = 0; i < nums.length; i++) {
            int val = Math.abs(nums[i]) - 1;
            if(nums[val] > 0) {
                nums[val] = -nums[val];
            }
        }
        
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] > 0) {
                ret.add(i+1);
            }
        }
        return ret;
	}

}