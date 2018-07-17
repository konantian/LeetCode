import java.util.*;

public class findLUSlength{
	public static void main(String args[]){
		String a="aba";
		String b="cdc";
		System.out.println(find_length(a,b));
	}

	public static int find_length(String a, String b) {
        if (a.equals(b))
            return -1;
        return Math.max(a.length(), b.length());
    }
}