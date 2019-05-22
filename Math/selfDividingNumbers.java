import java.util.*;

public class selfDividingNumbers{
	public static void main(String args[]){
		int left = 1;
		int right = 22;
		System.out.println(SelfDividingNumbers(left,right));
	}

	public static boolean canDivideByItself(final int n) {
	        boolean can = true;
	        int t = n;
	        while (t > 0) {
	            final int digit = t % 10;
	            if ((digit == 0) || (n % digit != 0)) {
	                can = false;
	                break;
	            }
	            t /= 10;
	        }
	        return can;
	    }
	    
	public static List<Integer> SelfDividingNumbers(int left, int right) {
	    final List<Integer> numbers = new ArrayList<>();

	    for (int i = left; i <= right; i++) {
	        if (canDivideByItself(i)) {
	            numbers.add(i);
	        }
	    }

	    return numbers;
	}
}

