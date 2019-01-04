import java.util.*;

class reverseOnlyLetters{
	public static void main(String args[]){
		String S = "Test1ng-Leet=code-Q!";
		System.out.println(ReverseOnlyLetters(S));

	}

	public static String ReverseOnlyLetters(String S) {
        Stack<Character> letters = new Stack<Character>();
        for (char c: S.toCharArray())
            if (Character.isLetter(c))
                letters.push(c);

        StringBuilder ans = new StringBuilder();
        for (char c: S.toCharArray()) {
            if (Character.isLetter(c))
                ans.append(letters.pop());
            else
                ans.append(c);
        }

        return ans.toString();
    }
}