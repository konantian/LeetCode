import java.util.*;

public class transpose{
	public static void main(String args[]){
		int A[][]={{1,2,3},{4,5,6},{7,8,9}};
		int result[][]=Transpose(A);
		System.out.println(Arrays.deepToString(result));
	}

	public static int[][] Transpose(int[][] A) {
        int M = A.length, N = A[0].length;
        int[][] B = new int[N][M];
        for (int j = 0; j < N; j++)
            for (int i = 0; i < M; i++)
                B[j][i] = A[i][j];
        return B;
    }
}