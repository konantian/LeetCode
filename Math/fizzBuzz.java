import java.util.*;

public class fizzBuzz{
	public static void main(String args[]){
		int n=15;
		List<String> result=fizz_buzz(n);
		System.out.println(Arrays.toString(result.toArray()));
	}

	public static List<String> fizz_buzz(int n) {
        List<String> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                list.add("FizzBuzz");
            } else if (i % 3 == 0) {
                list.add("Fizz");
            } else if (i % 5 == 0) {
                list.add("Buzz");
            } else {
                list.add(String.valueOf(i));
            }
        }
        return list;
    }
}