import java.util.*;
public class isMonotonic{
	public static void main(String args[]){
		int A[] = {1,2,3,4};
		System.out.println(IsMonotonic(A));
	}

	public static boolean IsMonotonic(int A[]){
		boolean isGreat = false;
		boolean isLess = false;

		for(int i=1;i<A.length;i++){

			if(A[i-1] > A[i]) isGreat = true;
			if(A[i-1] < A[i]) isLess = true;
			
			if(isLess == true && isGreat == true) return false;
		}

		return true;
	}

}