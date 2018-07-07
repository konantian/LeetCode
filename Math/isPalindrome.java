public class isPalindrome{
	public static void main(String args[]){
		int x = 1221;
		boolean result=is_palindrome(x);
		System.out.println(result);	
	}

	public static boolean is_palindrome(int x){
        if(x<0){
            return false;
        }

        int temp = x;
        int rec = 0;
        while(temp>0){
            rec = rec * 10 + temp % 10;  //将数字翻转，首先取最后一位
            temp = temp / 10;  //取一位就减少一位
        }
        return x == rec;
    }
}