import java.util.*;
public class sortedSquares{
	public static void main(String args[]){

		int A[] = {-4,-1,0,3,10};
		System.out.println(Arrays.toString(SortedSquares(A)));
	}

	public static int[] SortedSquares(int[] A) {
        int n = A.length;
        int[] result = new int[n];
        int i = 0, j = n - 1;
        for (int p = n - 1; p >= 0; p--) {
            if (Math.abs(A[i]) > Math.abs(A[j])) {
                result[p] = A[i] * A[i];
                i++;
            } else {
                result[p] = A[j] * A[j];
                j--;
            }
        }
        return result;
    }
}