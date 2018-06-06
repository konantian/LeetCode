import java.util.*;

public class missingNumber{
	public static void main(String[] args){
		int array[]={3,1,0};
		int number=miss_numberB(array);
		System.out.println(number);
	}

	public static int miss_numberA(int nums[]){
		int len=nums.length;
		int sum=((len+1)*len)/2;
		for(int i =0;i<len;i++){
			sum-=nums[i];
		}

		return sum;
	}

	public static int miss_numberB(int nums[]){
		Arrays.sort(nums);
		int left=0;
		int right=nums.length;
		int mid=(left+right)/2;
		while(left<right){
			mid=(left+right)/2;
			if(nums[mid]>mid) right= mid;
			else left=mid+1;
		}

		return left;
	}
}