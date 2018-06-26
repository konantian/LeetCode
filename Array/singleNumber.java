public class singleNumber{
	public static void main(String args[]){
		int array[]={4,1,2,1,2};
		int number=single_number(array);
		System.out.println(number);
	}

	public static int single_number(int[] nums) {
    int ans =0;
    
    int len = nums.length;
    for(int i=0;i!=len;i++)
        ans ^= nums[i];
    
    return ans;
    
	}

}