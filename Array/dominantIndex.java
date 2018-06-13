public class dominantIndex{
	public static void main(String[] args){
		int array[]={3,6,1,0};
		int index=dominant_index(array);
		System.out.println(index);
	}

	public static int dominant_index(int[] nums) {
        int maxIndex = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] > nums[maxIndex])
                maxIndex = i;
        }
        for (int i = 0; i < nums.length; ++i) {
            if (maxIndex != i && nums[maxIndex] < 2 * nums[i])
                return -1;
        }
        return maxIndex;
    }
}