public class isPowerOfTwo{
	public static void main(String args[]){
		int n = 218;
		boolean result=is_poweroftwo(n);
		System.out.println(result);
	}

	public static boolean is_poweroftwo(int n) {
    	return ((n & (n-1))==0 && n>0);
	}
}