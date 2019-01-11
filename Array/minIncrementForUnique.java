class minIncrementForUnique{
	public static void main(String args[]){
		int A[] = {2,2,2,3};
		System.out.println(MinIncrementForUnique(A));
	}

	public static int MinIncrementForUnique(int[] A) {
        int[] count = new int[100000];
        for (int x: A) count[x]++;

        int ans = 0, taken = 0;

        for (int x = 0; x < 100000; ++x) {
            if (count[x] >= 2) {
                taken += count[x] - 1;
                ans -= x * (count[x] - 1);
            }
            else if (taken > 0 && count[x] == 0) {
                taken--;
                ans += x;
            }
        }

        return ans;
    }
}