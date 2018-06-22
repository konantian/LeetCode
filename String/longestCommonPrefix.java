import java.util.*;

public class longestCommonPrefix{
	public static void main(String args[]){
		String array[]={"flower","flow","flight"};
		String common=longest_prefix(array);
		System.out.println(common);
	}

	public static String longest_prefix(String[] strs) {
    	if (strs.length == 0) return "";
    	String prefix = strs[0];
    	for (int i = 1; i < strs.length; i++)
        	while (strs[i].indexOf(prefix) != 0) {
            	prefix = prefix.substring(0, prefix.length() - 1);
            	if (prefix.isEmpty()) return "";
        	}        
    return prefix;
	}
}