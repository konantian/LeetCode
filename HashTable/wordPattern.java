import java.util.*;

public class wordPattern{
	public static void main(String args[]){
		String pattern="abba";
		String str="dog cat cat dog";
		boolean result=word_pattern(pattern,str);
		System.out.println(result);
	}

	public static boolean word_pattern(String pattern, String str) {
	    String[] words = str.split(" ");
	    if (words.length != pattern.length())
	        return false;
	    HashMap index = new HashMap<String,Integer>();
	    for (Integer i=0; i<words.length; ++i)
	        if (index.put(pattern.charAt(i), i) != index.put(words[i], i))
	            return false;
	    return true;
	}
}