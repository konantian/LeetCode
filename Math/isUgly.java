import java.util.*;

class isUgly{
	public static void main(String args[]){
		System.out.println(IsUgly(6));
		System.out.println(IsUgly(14));
	}

	public static boolean IsUgly(int num){
		for (int i=2; i<6 && num>0; i++){
    		while (num % i == 0){
        		num /= i;
    		}
        }
		return num == 1;
	}
}