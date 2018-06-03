/*
Algorithm

This solution follows the logic used in Approach 2 itself
but with only a slight variation. In this case, instead of 
looking for every peak following a valley, we can simply 
go on crawling over the slope and keep on adding the profit 
obtained from every consecutive transaction. In the end
we will be using the peaks and valleys effectively, 
but we need not track the costs corresponding to the peaks 
and valleys along with the maximum profit, but we can directly 
keep on adding the difference between the consecutive numbers of
the array if the second number is larger than the first one, and
at the total sum we obtain will be the maximum profit. 
This approach will simplify the solution. This can be made clearer by taking this example:


[1, 7, 2, 3, 6, 7, 6, 7]
*/

public class BestTimeToBuyAndSellStockII{
	public static void main(String[] args){
		int array[]={7,1,5,3,6,4};
		int profit=max_profit(array);
		System.out.println("The max profit is: "+profit);
	}

	public static int max_profit(int prices[]){
		int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
	}
}