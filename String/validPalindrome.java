public class validPalindrome{
	public static void main(String args[]){
		String s = "cbbcc";
		boolean result=valid_palindrome(s);
		System.out.println(result);
	}

	public static boolean valid_palindrome(String s) {
    	int l = -1, r = s.length();
    	while (++l < --r) 
        	if (s.charAt(l) != s.charAt(r)) return isPalindromic(s, l, r+1) || isPalindromic(s, l-1, r);
    	return true;
	}

	public static boolean isPalindromic(String s, int l, int r) {
    	while (++l < --r) 
        	if (s.charAt(l) != s.charAt(r)) return false;
    	return true;
	}
}