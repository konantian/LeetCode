import java.util.*;

public class reverseString{
	public static void main(String args[]){
		String s="helloworld";
		String result=reverse_stringB(s);
		System.out.println(result);
	}


	public static String reverse_stringA(String s) {
        StringBuilder sb = new StringBuilder(s);
        return sb.reverse().toString();
    }

    //method 2: use swap method
    public static String reverse_stringB(String s){
        if(s == null || s.length() == 0)
            return "";
        char[] cs = s.toCharArray();
        int begin = 0, end = s.length() - 1;
        while(begin <= end){
            char c = cs[begin];
            cs[begin] = cs[end];
            cs[end] = c;
            begin++;
            end--;
        }
        
        return new String(cs);
    }
}