import java.util.*;

class numSpecialEquivGroups{
	public static void main(String args[]){
		String A[] = {"a","b","c","a","c","c"};
		System.out.println(NumSpecialEquivGroups(A));
	}

	public static int NumSpecialEquivGroups(String[] A) {
        Set<String> seen = new HashSet();
        for (String S: A) {
            int[] count = new int[52];
            for (int i = 0; i < S.length(); ++i)
                count[S.charAt(i) - 'a' + 26 * (i % 2)]++;
            seen.add(Arrays.toString(count));
        }
        return seen.size();
    }
}