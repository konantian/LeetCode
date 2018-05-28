import java.util.Arrays;

public class PlusOne{
	public static void main(String [] args){
		int array[]={9};
		array=plus_one(array);
		System.out.println(Arrays.toString(array));
	}

	public static int[] plus_one(int digits[]){
		for(int i=digits.length-1;i>=0;i--){
			if(digits[i] < 9){
				digits[i]++;
				return digits;
			}

			digits[i] = 0;
		}

		int number[]=new int [digits.length+1];

		number[0] = 1;

		return number;
	}
}