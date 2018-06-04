import java.util.*;

public class majorityElement{
	public static void main(String[] args){
		int array[]={2,2,1,1,1,2,2};
		int element=majorityElement3(array);
		System.out.println("The majority element is:"+element);
	}

	public static int majorityElement2(int[] nums) {
    Map<Integer, Integer> myMap = new HashMap<Integer, Integer>();
    //Hashtable<Integer, Integer> myMap = new Hashtable<Integer, Integer>();
    int ret=0;
    for (int num: nums) {
        if (!myMap.containsKey(num))
            myMap.put(num, 1);
        else
            myMap.put(num, myMap.get(num)+1);
        if (myMap.get(num)>nums.length/2) {
            ret = num;
            break;
        }
    }
    return ret;
	}

	// Moore voting algorithm
	public static int majorityElement3(int[] nums) {
    	int count=0, ret = 0;
    	for (int num: nums) {
        	if (count==0)
            	ret = num;
        	if (num!=ret)
           		count--;
        	else
            	count++;
    	}
    	return ret;
	}
}