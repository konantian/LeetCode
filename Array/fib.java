import java.util.*;

public class fib{
	public static void main(String args[]){
		int N = 10;
		System.out.println(Fib(N));
	}

	public static int Fib(int N){
		if(N < 2) return N;
        ArrayList<Integer> result = new ArrayList<>();
        result.add(0);
        result.add(1);
        int n = N-result.size()+1;
        for(int i = 0;i<n;i++){
            result.add(result.get(result.size()-1)+result.get(result.size()-2));
        }
        return result.get(result.size()-1);
	}

	public static int Fib2(int N){
		if(N <= 1)
            return N;
        
		int a = 0, b = 1;
		
		while(N-- > 1)
		{
			int sum = a + b;
			a = b;
			b = sum;
		}
        return b;
	}
}