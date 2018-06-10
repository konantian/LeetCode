public class findUnsortedSubarray{
	public static void main(String[] args){
		int array[]={2,6,4,8,10,9,15};
		int number=find_array(array);
		System.out.println(number);
	}

	public static int find_array(int nums[]){
		int n = nums.length, beg = -1, end = -2, min = nums[n-1], max = nums[0];
    	for (int i=1;i<n;i++) {
      		max = Math.max(max, nums[i]);
      		min = Math.min(min, nums[n-1-i]);
      		if (nums[i] < max) end = i;
      		if (nums[n-1-i] > min) beg = n-1-i; 
    	}
    	return end - beg + 1;
	}
}