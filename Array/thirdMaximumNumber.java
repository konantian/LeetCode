import java.util.*;

public class thirdMaximumNumber{
	public static void main(String[] args){
		int array[]={2,2,3,1};
		int number=0;
		List<Integer> nums = new ArrayList<>();
		for(int x:array){
			nums.add(x);
		}
		Set<Integer> set=new HashSet<>();
		set.addAll(nums);
		nums.clear();
		nums.addAll(set);
		Collections.sort(nums);
		if(nums.size() < 3) number=nums.get(nums.size()-1);
		number=nums.get(nums.size()-3);
		System.out.println(number);
	}


}