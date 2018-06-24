import java.util.*;

public class reverseVowels{
	public static void main(String args[]){
		String s="hello";
		String reverse=reverse_vowels(s);
		System.out.println(reverse);
	}

	public static String reverse_vowels(String s) {
	    if(s == null || s.length()==0) return s;
	    String vowels = "aeiouAEIOU";
	    char[] chars = s.toCharArray();
	    int start = 0;
	    int end = s.length()-1;
	    while(start<end){
	        
	        while(start<end && !vowels.contains(chars[start]+"")){
	            start++;
	        }
	        
	        while(start<end && !vowels.contains(chars[end]+"")){
	            end--;
	        }
	        
	        char temp = chars[start];
	        chars[start] = chars[end];
	        chars[end] = temp;
	        
	        start++;
	        end--;
	    }
	    return new String(chars);
	}
}