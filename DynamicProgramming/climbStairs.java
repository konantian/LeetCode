public class climbStairs{
	public static void main(String args[]){
		int n = 30;
		int result=climb_stairs(n);
		System.out.println(result);
	}

	public static int climb_stairs(int n) {
        if (n == 1) {
            return 1;
        }
        int first = 1;
        int second = 2;
        for (int i = 3; i <= n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }
}