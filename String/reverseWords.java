import java.util.*;

public class reverseWords{
	public static void main(String args[]){
		String s="Let's take LeetCode contest";
		String output=reverse_words(s);
		System.out.println(output);
	}

	public static String reverse_words(String s) {
        String[] str = s.split(" ");
        for (int i = 0; i < str.length; i++) str[i] = new StringBuilder(str[i]).reverse().toString();
        StringBuilder result = new StringBuilder();
        for (String st : str) result.append(st + " ");
        return result.toString().trim();
    } 
}