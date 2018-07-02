import java.util.*;

public class mostCommonWord{
	public static void main(String args[]){
		String paragraph="Bob hit a ball, the hit BALL flew far after it was hit.";
		String banned[]={"hit"};
		String word=most_commonword(paragraph,banned);
		System.out.println(word);
	}

	public static String most_commonword(String p, String[] banned) {
        Set<String> ban = new HashSet<>(Arrays.asList(banned));
        Map<String, Integer> count = new HashMap<>();
        String[] words = p.replaceAll("\\pP" , "").toLowerCase().split("\\s+");
        for (String w : words) if (!ban.contains(w)) count.put(w, count.getOrDefault(w, 0) + 1);
        return Collections.max(count.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}