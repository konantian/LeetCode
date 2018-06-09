import java.util.*;

public class findPairs{
	public static void main(String[] args){
		int nums[]={3, 1, 4, 1, 5};
		int k = 2;
		int number=find_pairs(nums,k);
		System.out.println(number);
	}

	public static int find_pairs(int nums[],int k){
		if (k < 0) { return 0; }

        Set<Integer> starters = new HashSet<Integer>();
        Set<Integer> uniqs = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (uniqs.contains(nums[i] - k)) starters.add(nums[i] - k);
            if (uniqs.contains(nums[i] + k)) starters.add(nums[i]);
            uniqs.add(nums[i]);
        }

        return starters.size();
    }
}