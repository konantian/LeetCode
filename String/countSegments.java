public class countSegments{
	public static void main(String args[]){
		String s="  Hello World I love you  ";
		int count=count_segments(s);
		System.out.println(count);
	}

	public static int count_segments(String s) {
        int segmentCount = 0;

        for (int i = 0; i < s.length(); i++) {
            if ((i == 0 || s.charAt(i-1) == ' ') && s.charAt(i) != ' ') {
                segmentCount++;
            }
        }

        return segmentCount;
    }
}