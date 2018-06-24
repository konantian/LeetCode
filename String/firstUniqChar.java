public class firstUniqChar{
	public static void main(String args[]){
		String s="loveleetcode";
		int index=first_unique(s);
		System.out.println(index);
	}

	public static int first_unique(String s) {
        int freq [] = new int[26];
        for(int i = 0; i < s.length(); i ++)
            freq [s.charAt(i) - 'a'] ++;
        for(int i = 0; i < s.length(); i ++)
            if(freq [s.charAt(i) - 'a'] == 1)
                return i;
        return -1;
    }
}