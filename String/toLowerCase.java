import java.util.*;

public class toLowerCase{
	public static void main(String args[]){
		String str="Hello";
		System.out.println(to_lowercase(str));
	}

	public static String to_lowercase(String str){
		int diff = 'A' - 'a';
        StringBuilder lower = new StringBuilder();
        for (char c : str.toCharArray())
            if (c >= 'A' && c <= 'Z')
                lower.append((char)(c - diff));
            else lower.append(c);
        return lower.toString();
	}
}