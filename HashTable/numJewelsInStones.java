import java.util.*;

public class numJewelsInStones{
	public static void main(String args[]){
		String J="aA";
		String S="aAAbbbb";
		int count=num_jewel(J,S);
		System.out.println(count);
	}

	public static int num_jewel(String J, String S) {
        int res = 0;
        Set<Character> setJ = new HashSet<Character>();
        for (char j: J.toCharArray()) setJ.add(j);
        for (char s: S.toCharArray()) if (setJ.contains(s)) res++;
        return res;
    }
}