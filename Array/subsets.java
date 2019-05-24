import java.util.*;

public class subsets{
	public static void main(String args[]){
		int nums[] = {1,2,3};
		System.out.println(Subsets(nums));
	}

	public static List<List<Integer>> Subsets(int nums[]){
		Arrays.sort(nums); // make sure subsets are ordered
	    List<List<Integer>> result = new ArrayList<>();
	    result.add(new ArrayList<>()); // start with empty set
	    for (int i = 0; i < nums.length; ++i) {
	        for (int j = 0, size = result.size(); j < size; ++j) { // remember
	            List<Integer> subset = new ArrayList<>(result.get(j)); // copy a new one
	            subset.add(nums[i]); // expand
	            result.add(subset); // collect
	        }
	    }
	    return result;

	}
}