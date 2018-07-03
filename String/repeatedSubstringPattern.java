public class repeatedSubstringPattern{
	public static void main(String args[]){
		String s="abcabcabc";
		boolean result=repeated_substring(s);
		System.out.println(result);
	}

	public static boolean repeated_substring(String str) {
        String s = str + str;
        return s.substring(1, s.length() - 1).contains(str);
    }
}