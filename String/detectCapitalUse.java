public class detectCapitalUse{
	public static void main(String args[]){
		String word="USA";
		boolean result=detect_capital(word);
		System.out.println(result);

	}

	public static boolean detect_capital(String word) {
        if (word.length() < 2) return true;
        if (word.toUpperCase().equals(word)) return true;
        if (word.substring(1).toLowerCase().equals(word.substring(1))) return true;
        return false;
	}
}