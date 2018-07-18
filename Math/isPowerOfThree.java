public class isPowerOfThree{
	public static void main(String args[]){
		int n = 27;
		System.out.println(is_powerofthree(n));
	}

	public static boolean is_powerofthree(int n){
		return n > 0 && 1162261467 % n == 0;
	}
}