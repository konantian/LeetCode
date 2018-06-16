public class checkPossibility{
	public static void main(String[] args){
		int array[]={2,3,3,2,4};
		boolean result=check_possibility(array);
		System.out.println(result);
	}

	public static boolean check_possibility(int[] nums) {
        int cnt = 0;                                                                    //the number of changes
        for(int i = 1; i < nums.length && cnt<=1 ; i++){
            if(nums[i-1] > nums[i]){
                cnt++;
                if(i-2<0 || nums[i-2] <= nums[i])nums[i-1] = nums[i];                    //modify nums[i-1] of a priority
                else nums[i] = nums[i-1];                                                //have to modify nums[i]
            }
        }
        return cnt<=1; 
    }
}