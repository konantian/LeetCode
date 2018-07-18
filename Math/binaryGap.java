public class binaryGap{
	public static void main(String args[]){
		int N=22;
		System.out.println(binary_gap(N));
	}

	public static int binary_gap(int N) {
        int res = 0;
        for (int d = -32; N > 0; N /= 2, d++)
            if (N % 2 == 1) {
                res = Math.max(res, d);
                d = 0;
            }
        return res;
    }
}