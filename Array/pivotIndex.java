public class pivotIndex{
	public static void main(String[] args){
		int array[]={1, 7, 3, 6, 5, 6};
		int index=pivot_index(array);
		System.out.println(index);
	}

	public static int pivot_index(int nums[]){
		int part1 = 0, part2 = 0;
        for (int x: nums) part2 += x;
        for(int i =0;i<nums.length;i++){
        	part2-=nums[i];
        	if(part1 == part2) return i;
        	part1+=nums[i];
        }

        return -1;
	}
}