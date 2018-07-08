public class titleToNumber{
	public static void main(String args[]){
		String s = "ZY";
		int result=title_number(s);
		System.out.println(result);
	}

	public static int title_number(String s) {
    
        int result  = 0;
        for (int i = 0; i < s.length(); i++){
            result *= 26;
            result += ((s.charAt(i) - 'A') + 1);    
        }
    
        return result;
    }
}