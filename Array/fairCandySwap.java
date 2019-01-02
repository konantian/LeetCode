import java.util.*;
public class fairCandySwap{
	public static void main(String args[]){
		int A[] = {1,2,5};
		int B[] = {2,4};
		System.out.println(Arrays.toString(FairCandySwap(A,B)));
	}

public static int[] FairCandySwap(int[] A, int[] B) {
		int sumA = 0, sumB = 0;
		Set<Integer> set = new HashSet<>();
		for (int a : A) {
			sumA += a;
		}
		for (int b : B) {
			set.add(b);
			sumB += b;
		}
		int diff = (sumA - sumB) / 2;
		int[] res = new int[2];
		for (int a : A) {
			if (set.contains(a - diff)) {
				res[0] = a;
				res[1] = a - diff;
				break;
			}
		}
		return res;
	}
}