import java.util.*;

class findMedianSortedArrays{
	public static void main(String args[]){
		int nums1[] = {1,2};
		int nums2[] = {3,4};
		System.out.println(FindMedianSortedArrays(nums1,nums2));
	}

	public static double FindMedianSortedArrays(int nums1[],int nums2[]){
		List<Integer> num = new ArrayList<>();
        int i = 0;
        int j = 0;
        while(i<nums1.length & j<nums2.length){
            if(nums1[i]<=nums2[j]){
                num.add(nums1[i]);
                i++;
            }else{
                num.add(nums2[j]);
                j++;
            }
        }
        for(;i<nums1.length;i++) num.add(nums1[i]);
        for(;j<nums2.length;j++) num.add(nums2[j]);
        
        double result;
        if(num.size() % 2 == 0){
            int A = num.get(num.size()/2);
            int B = num.get(num.size()/2-1);
            
            result = (double)(A+B)/2;
            return result;
        } 
        
        int index = (int)Math.floor(num.size()/2);
        result = num.get(index);
        return result;

	}
}