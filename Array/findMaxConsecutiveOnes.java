public class findMaxConsecutiveOnes{
	public static void main(String[] args){
		int array[]={1,1,0,1,1,1};
		int number=find_consecutive(array);
		System.out.println(number);
	}
    public static int find_consecutive(int[] nums) {
        int count=0;
        int amount=0;
        for(int i = 0;i<nums.length;i++){
        	if(nums[i] == 1) count++;
        	else count=0;

        	if(amount<count) amount= count;
        }

        return amount;
    }
}