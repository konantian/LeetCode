import java.util.*;

class hasGroupsSizeX{
	public static void main(String args[]){
		int desk[] = {1,2,3,4,4,3,2,1};
		System.out.println(HasGroupsSizeX(desk));
	}

	public static boolean HasGroupsSizeX(int[] deck) {
        int[] count = new int[10000];
        for (int c: deck)
            count[c]++;

        int g = -1;
        for (int i = 0; i < 10000; ++i)
            if (count[i] > 0) {
                if (g == -1)
                    g = count[i];
                else
                    g = gcd(g, count[i]);
            }

        return g >= 2;
    }

    public static int gcd(int x, int y) {
        return x == 0 ? y : gcd(y%x, x);
    }
}