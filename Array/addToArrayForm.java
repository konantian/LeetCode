import java.util.*;
public class addToArrayForm{
	public static void main(String args[]){

		int A[] = {1,2,0,0};
		int K = 34;
		ArrayList<Integer> numberSum = AddToArrayForm(A,K);
        for (Integer num : numberSum){
            System.out.println(num);
        }

	}

	public static ArrayList<Integer> AddToArrayForm(int[] A, int K) {
        int N = A.length;
        int cur = K;
        ArrayList<Integer> ans = new ArrayList<Integer>();

        int i = N;
        while (--i >= 0 || cur > 0) {
            if (i >= 0)
                cur += A[i];
            ans.add(cur % 10);
            cur /= 10;
        }

        Collections.reverse(ans);
        return ans;
    }
}