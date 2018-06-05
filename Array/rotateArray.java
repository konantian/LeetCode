import java.util.*;

public class rotateArray{
	public static void main(String[] args){
		int array[]={1,2,3,4,5,6,7};
		int k = 3;
		rotate(array,k);
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
}