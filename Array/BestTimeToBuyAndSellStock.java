import java.lang.Math;

public class BestTimeToBuyAndSellStock{
	public static void main(String[] args){
		int array[]={7,1,5,3,6,4};
		int profit=max_profit(array);
		int profitB=maxProfit(array);
		System.out.println("The max profit is: "+profit);
		System.out.println("The max profit is: "+profitB);
	}

	public static int max_profit(int prices[]){
		int maxCur=0;
		int maxSoFar=0;
		for(int i = 1;i<prices.length;i++){
			maxCur+=prices[i]-prices[i-1];
			maxCur=Math.max(0,maxCur);
			maxSoFar=Math.max(maxCur,maxSoFar);
		}

		return maxSoFar;
	}

	public static int maxProfit(int prices[]){
		int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
	}
}