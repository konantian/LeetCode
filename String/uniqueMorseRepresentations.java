import java.util.*;

public class uniqueMorseRepresentations{
	public static void main(String args[]){
		String words[]={"gin", "zen", "gig", "msg"};
		int count=unique_morse(words);
		System.out.println(count);
	}

	public static int unique_morse(String[] words) {
        String[] MORSE = new String[]{".-","-...","-.-.","-..",".","..-.","--.",
                         "....","..",".---","-.-",".-..","--","-.",
                         "---",".--.","--.-",".-.","...","-","..-",
                         "...-",".--","-..-","-.--","--.."};

        Set<String> seen = new HashSet<String>();
        for (String word: words) {
            StringBuilder code = new StringBuilder();
            for (char c: word.toCharArray())
                code.append(MORSE[c - 'a']);
            seen.add(code.toString());
        }

        return seen.size();
    }
}