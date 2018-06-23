public class canConstruct{
	public static void main(String args[]){
		String ransomNote="aa";
		String magazine="aab";
		boolean result=can_construct(ransomNote,magazine);
		System.out.println(result);
	}

	public static boolean can_construct(String ransomNote, String magazine) {
        int[] arr = new int[26];
        for (int i = 0; i < magazine.length(); i++) {
            arr[magazine.charAt(i) - 'a']++;
        }
        for (int i = 0; i < ransomNote.length(); i++) {
            if(--arr[ransomNote.charAt(i)-'a'] < 0) {
                return false;
            }
        }
        return true;
    }
}