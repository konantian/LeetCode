import java.util.*;

class sortArrayByParityII{
	public static void main(String args[]){
		int A[] = {4,2,5,7};
		System.out.println(Arrays.toString(SortArrayByParityII(A)));
	}

	public static int[] SortArrayByParityII(int A[]){
		int N = A.length;
        int[] ans = new int[N];

        int t = 0;
        for (int x: A) if (x % 2 == 0) {
            ans[t] = x;
            t += 2;
        }

        t = 1;
        for (int x: A) if (x % 2 == 1) {
            ans[t] = x;
            t += 2;
        }

        return ans;
	}
}