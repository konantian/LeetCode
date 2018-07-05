public class reverseInteger{
	public static void main(String args[]){
		int x = - 12345;
		int result=reverse_integer(x);
		System.out.println(result);
	}

	public static int reverse_integer(int x){
    	int result = 0;

    	while (x != 0){
        	int tail = x % 10;
        	int newResult = result * 10 + tail;
        	if ((newResult - tail) / 10 != result) return 0; 
        	result = newResult;
        	x = x / 10;
    	}

    	return result;
	}
}