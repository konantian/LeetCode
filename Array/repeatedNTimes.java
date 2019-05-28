public class repeatedNTimes{
	public static void main(String args[]){
		int A = {1,2,3,3};
		System.out.println(RepeatedNTimes(A));
	}

	public int RepeatedNTimes(int[] A) {
        Map<Integer, Integer> count = new HashMap();
        for (int x: A) {
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        for (int k: count.keySet())
            if (count.get(k) > 1)
                return k;

        throw null;
    }
}