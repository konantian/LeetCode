import java.util.*;

public class imageSmoother{
	public static void main(String[] args){
		int matrix[][]={{1,1,1},{1,0,1},{1,1,1}};
		int smooth_matrix[][]=image_smoother(matrix);
		System.out.println(Arrays.deepToString(smooth_matrix));
	}

	public static int[][] image_smoother(int[][] M) {
        int R = M.length, C = M[0].length;
        int[][] ans = new int[R][C];

        for (int r = 0; r < R; ++r)
            for (int c = 0; c < C; ++c) {
                int count = 0;
                for (int nr = r-1; nr <= r+1; ++nr)
                    for (int nc = c-1; nc <= c+1; ++nc) {
                        if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                            ans[r][c] += M[nr][nc];
                            count++;
                        }
                    }
                ans[r][c] /= count;
            }
        return ans;
    }
}