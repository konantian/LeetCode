public class isPowerOfFour{
	public static void main(String args[]){
		int n = 16;
		System.out.println(is_poweroffour(n));
	}

	public static boolean is_poweroffour(int num){
		return num > 0 && (num&(num-1)) == 0 && (num & 0x55555555) != 0;
		//return num > 0 && (num & (num-1)) == 0 && (num-1) % 3 == 0;
	}
}