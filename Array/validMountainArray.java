import java.util.*;

class validMountainArray{
	public static void main(String args[]){
		int A[] = {0,3,2,1};
		System.out.println(ValidMountainArray(A));
	}

	public static boolean ValidMountainArray(int[] A) {
        int N = A.length;
        int i = 0;

        // walk up
        while (i+1 < N && A[i] < A[i+1])
            i++;

        // peak can't be first or last
        if (i == 0 || i == N-1)
            return false;

        // walk down
        while (i+1 < N && A[i] > A[i+1])
            i++;

        return i == N-1;
    }
}