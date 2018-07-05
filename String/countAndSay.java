import java.util.*;

public class countAndSay{
	public static void main(String args[]){
		int n = 7;
		String result=count_andsay(n);
		System.out.println(result);
	}

	public static String count_andsay(int n){
		if(n==1) return "1";

		String string=count_andsay(n-1);
		char initial=string.charAt(0);
		int count=0;
		String result="";
		for(int i = 0;i<string.length();i++){
			if(string.charAt(i) == initial){
				count++;
				if(i == string.length()-1) result+=Integer.toString(count)+initial;

			}

			else{
				result+=Integer.toString(count)+initial;
				initial=string.charAt(i);
				count=1;

				if(i == string.length()-1) result+=Integer.toString(count)+initial;
			}
		}

		return result;
	}
}