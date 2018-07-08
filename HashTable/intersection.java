import java.util.*;

public class intersection{
	public static void main(String args[]){
		int nums1[]={1,2,2,1};
		int nums2[]={2,2};
		int result[]=intersection_arrays(nums1,nums2);
		System.out.println(Arrays.toString(result));
	}

	public static int[] intersection_arrays(int[] nums1, int[] nums2) {
        Set<Integer> set = new HashSet<>();
        Set<Integer> intersect = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            set.add(nums1[i]);
        }
        for (int i = 0; i < nums2.length; i++) {
            if (set.contains(nums2[i])) {
                intersect.add(nums2[i]);
            }
        }
        int[] result = new int[intersect.size()];
        int i = 0;
        for (Integer num : intersect) {
            result[i++] = num;
        }
        return result;
    }
}