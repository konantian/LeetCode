public class findTheDifference{
	public static void main(String args[]){
		String s= "a";
		String t= "aa";
		char result=find_differenceA(s,t);
		System.out.println(result);
	}

	//Using bit manipulation
	public static char find_differenceA(String s, String t) {
		char c = 0;
		for (int i = 0; i < s.length(); ++i) {
			c ^= s.charAt(i);
		}
		for (int i = 0; i < t.length(); ++i) {
			c ^= t.charAt(i);
		}
		return c;
	}

	public static char find_differenceB(String s, String t) {
        int charCode = t.charAt(s.length());
        // Iterate through both strings and char codes
        for (int i = 0; i < s.length(); ++i) {
              charCode -= (int)s.charAt(i);
              charCode += (int)t.charAt(i); 
        }
        return (char)charCode;
    }
}