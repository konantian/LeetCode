import java.util.*;

public class findMaxAverage{
	public static void main(String[] args){
		int array[]={1,12,-5,-6,50,3};
		int k = 4;
		double average=find_average(array,k);
		System.out.println(average);
	}

	public static double find_average(int nums[],int k){
		double sum=0;
		for(int i=0;i<k;i++) sum+=nums[i];
		double average=sum;
		for(int i=k;i<nums.length;i++){
			sum+=nums[i]-nums[i-k];
			average=Math.max(average,sum);
		}

		return average/k;
	}
}