import java.util.*;

public class containsDuplicateII{
	public static void main(String[] args){
		int array[]={1,2,3,1,2,1};
		int k=5;
		boolean result=containsNearbyDuplicate(array,k);
		System.out.println(result);
	}


	public static boolean containsNearbyDuplicate(int[] nums, int k) {
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    for (int i = 0; i < nums.length; i++) {
        if (map.containsKey(nums[i])) {
            if (i - map.get(nums[i]) <= k) return true;
        }
        map.put(nums[i], i);
    }
    return false;
}
}