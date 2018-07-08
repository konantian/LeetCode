public class isAnagram{
	public static void main(String args[]){
		String s="";
		String t="";
		boolean result=is_anagram(s,t);
		System.out.println(result);
	}

	public static boolean is_anagram(String s, String t) {
	    if (s.length() != t.length()) {
	        return false;
	    }
	    int[] counter = new int[26];
	    for (int i = 0; i < s.length(); i++) {
	        counter[s.charAt(i) - 'a']++;
	        counter[t.charAt(i) - 'a']--;
	    }
	    for (int count : counter) {
	        if (count != 0) {
	            return false;
	        }
	    }
	    return true;
	}
}