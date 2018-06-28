public class checkRecord{
	public static void main(String args[]){
		String s="PPALLA";
		boolean result=check_recordB(s);
		System.out.println(result);
	}

	public static boolean check_recordA(String s) {
        if(s.indexOf("A") != s.lastIndexOf("A") || s.contains("LLL"))
            return false;
        return true;
    }

    public static boolean check_recordB(String s) {
    	return !s.matches(".*LLL.*|.*A.*A.*");
	}
}