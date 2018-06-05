import java.util.*;

public class containsDuplicate{
	public static void main(String[] args){
		int array[]={1,2,3,1};
		boolean exist=contain_duplicateB(array);
		System.out.println(exist);
	}

	public static boolean contain_duplicate(int nums[]){
		Set<Integer> set = new HashSet<Integer>();
		for(int i:nums){ 
			if(!set.add(i)) return true; //or, if(set.contains(x)) return true;
		}

		return false;
	}

	public static boolean contain_duplicateB(int nums[]){
		Arrays.sort(nums);
		for(int i = 1;i<nums.length;i++){
			if(nums[i] == nums[i-1]) return true;
		}

		return false;
	}
}