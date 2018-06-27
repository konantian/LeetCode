public class lengthOfLastWord{
	public static void main(String args[]){
		String s=" Hello World    ";
		int length=length_lastword(s);
		System.out.println(length);
	}

	public static int length_lastword(String s) {
    	return s.trim().length()-s.trim().lastIndexOf(" ")-1;
	}

	
}