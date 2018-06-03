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