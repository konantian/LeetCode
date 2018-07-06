import java.util.*;

public class isHappy{
	public static void main(String args[]){
		int n = 19;
		boolean result=is_happy(n);
		System.out.println(result);
	}

	public static boolean is_happy(int n) {
    	Set<Integer> inLoop = new HashSet<Integer>();
    	int squareSum,remain;
		while (inLoop.add(n)) {
			squareSum = 0;
			while (n > 0) {
		    	remain = n%10;
				squareSum += remain*remain;
				n /= 10;
			}
			if (squareSum == 1)
				return true;
			else
				n = squareSum;

		}
	return false;

	}
}