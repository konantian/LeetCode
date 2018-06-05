import java.util.*;

public class rotateArray{
	public static void main(String[] args){
		int array[]={1,2,3,4,5,6,7};
		int k = 3;
		rotateB(array,k);
		System.out.println(Arrays.toString(array));
	}

	public static void rotate(int nums[],int k){
		int a[]= new int[nums.length];
		for(int i =0;i<nums.length;i++){
			a[(i+k)%nums.length] = nums[i];
		}

		for(int i = 0;i<nums.length;i++){
			nums[i] = a[i];
		}
	}

	public static void rotateB(int nums[],int k){
		k %= nums.length;
		reverse(nums,0,nums.length-1);
		reverse(nums,0,k-1);
		reverse(nums,k,nums.length-1);
	}

	public static void reverse(int nums[],int start,int end){
		while(start < end){
			int temp = nums[start];
			nums[start] = nums[end];
			nums[end]=temp;
			start++;
			end--;

		}
	}
}