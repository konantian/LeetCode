public class strStr{
	public static void main(String args[]){
		String haystack="hello";
		String needle="ll";
		int index=find_index(haystack,needle);
		System.out.println(index);
	}

	public static int find_index(String haystack,String needle){
		for(int i=0;i<haystack.length()-needle.length()+1;i++){
			String substring=haystack.substring(i,i+needle.length());
			if(substring.equals(needle)) return i;
		}

		return -1;
	}
}