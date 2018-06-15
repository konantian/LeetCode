public class isOneBitCharacter{
	public static void main(String[] args){
		int array[]={1,1,1,0};
		boolean result=check_onebit(array);
		System.out.println(result);
	}

	public static boolean check_onebit(int bits[]){
		int i = 0;
        while (i < bits.length - 1) {
            i += bits[i] + 1;
        }
        return i == bits.length - 1;
	}

	public static boolean check_onebitB(int bits[]){
		int i = bits.length - 2;
        while (i >= 0 && bits[i] > 0) i--;
        return (bits.length - i) % 2 == 0;
	}
}