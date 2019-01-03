import java.util.*;

class sortArrayByParity{
	public static void main(String args[]){
		int A[] = {2,1,4,3};
		System.out.println(Arrays.toString(SortArrayByParity(A)));
	}

	public static int[] SortArrayByParity(int A[]){
		int temp;
		for(int i = 0,j=0;j<A.length;j++){
			if(A[j]%2 == 0){
				temp = A[i];
				A[i++] = A[j];
				A[j] = temp;
			}
		}
		return A;
	}
}