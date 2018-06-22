import java.util.*;

public class maxDistToClosest{
	public static void main(String args[]){
		int array[]={1,1,0,1,1,1};
		int result=max_dist(array);
		System.out.println(result);
	}

	public static int max_dist(int[] seats) {
        int res = 0, n = seats.length;
        for (int i = 0, zero = 0; i < n; ++i) if (seats[i] == 1) zero = 0; else res = Math.max(res, (++zero + 1) / 2);
        for (int i = 0, zero = 0; seats[i] == 0; ++i) res = Math.max(res, ++zero);
        for (int i = n - 1, zero = 0; seats[i] == 0; --i) res = Math.max(res, ++zero);
        return res;
    }
}