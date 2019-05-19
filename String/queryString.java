import java.util.*;

public class queryString{
	public static void main(String args[]){
		int N = 3;
		String S = "0110";
		System.out.println(QueryString(S,N));
	}

	public static boolean QueryString(String S, int N) {
        for (int i = N; i > N / 2; --i)
            if (!S.contains(Integer.toBinaryString(i)))
                return false;
        return true;
    }
}