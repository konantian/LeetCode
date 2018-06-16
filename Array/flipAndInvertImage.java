import java.util.*;

public class flipAndInvertImage{
	public static void main(String args[]){
		int A[][]={{1,1,0,0},{1,0,0,1},{0,1,1,1},{1,0,1,0}};
		int invert_A[][]=flip_image(A);
		System.out.println(Arrays.deepToString(invert_A));
	}

	public static int[][] flip_image(int A[][]){
		int C = A[0].length;
        for (int[] row: A)
            for (int i = 0; i < (C + 1) / 2; ++i) {
                int tmp = row[i] ^ 1;
                row[i] = row[C - 1 - i] ^ 1;
                row[C - 1 - i] = tmp;
            }

        return A;
	}
}