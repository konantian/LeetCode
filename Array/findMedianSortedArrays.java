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

    public static double FindMedianSortedArrays(int[] A, int[] B) {
        int m = A.length;
        int n = B.length;
        if (m > n) { // to ensure m<=n
            int[] temp = A; A = B; B = temp;
            int tmp = m; m = n; n = tmp;
        }
        int iMin = 0, iMax = m, halfLen = (m + n + 1) / 2;
        while (iMin <= iMax) {
            int i = (iMin + iMax) / 2;
            int j = halfLen - i;
            if (i < iMax && B[j-1] > A[i]){
                iMin = i + 1; // i is too small
            }
            else if (i > iMin && A[i-1] > B[j]) {
                iMax = i - 1; // i is too big
            }
            else { // i is perfect
                int maxLeft = 0;
                if (i == 0) { maxLeft = B[j-1]; }
                else if (j == 0) { maxLeft = A[i-1]; }
                else { maxLeft = Math.max(A[i-1], B[j-1]); }
                if ( (m + n) % 2 == 1 ) { return maxLeft; }

                int minRight = 0;
                if (i == m) { minRight = B[j]; }
                else if (j == n) { minRight = A[i]; }
                else { minRight = Math.min(B[j], A[i]); }

                return (maxLeft + minRight) / 2.0;
            }
        }
        return 0.0;
    }
}