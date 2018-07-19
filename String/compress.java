import java.util.*;

public class compress{
	public static void main(String args[]){
		char chars[]={'a','a','b','b','c','c','c'};
		int result=compress_string(chars);
		System.out.println(Arrays.toString(chars));
	}

	public static int compress_string(char[] chars) {
        int indexAns = 0, index = 0;
        while(index < chars.length){
            char currentChar = chars[index];
            int count = 0;
            while(index < chars.length && chars[index] == currentChar){
                index++;
                count++;
            }
            chars[indexAns++] = currentChar;
            if(count != 1)
                for(char c : Integer.toString(count).toCharArray()) 
                    chars[indexAns++] = c;
        }
        return indexAns;
    }
}