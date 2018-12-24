import java.util.*;

public class minCostClimbingStairs{
	public static void main(String args[]){
		int cost[] ={1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
		int finalCost = MinCostClimbingStairsB(cost);
		System.out.println(finalCost);
	}

	public static int MinCostClimbingStairsA(int[] cost){
		int f1 = 0;
		int f2 = 0;
		for(int i = cost.length-1;i >= 0;--i){
			int f0 = cost[i]+Math.min(f1,f2);
			f2 = f1;
			f1 = f0;
		}
		return Math.min(f1,f2);
	}

	public static int MinCostClimbingStairsB(int[] cost) {
        for (int i = 2; i < cost.length; i++) {
            cost[i] += Math.min(cost[i-1], cost[i-2]);
        }
        return Math.min(cost[cost.length-1], cost[cost.length-2]);
    }
}