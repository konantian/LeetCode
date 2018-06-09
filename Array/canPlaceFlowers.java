public class canPlaceFlowers{
	public static void main(String[] args){
		int array[]={0,0,0,1,0,0,0,0,0,1,0,1};
		int n = 3;
		boolean result=place_flowers(array,n);
		System.out.println(result);
	}

	public static boolean place_flowers(int flowerbed[],int n){
		int count = 0;
        for(int i = 0; i < flowerbed.length; i++) {
            if(flowerbed[i] == 0) {
	     //get next and prev flower bed slot values. If i lies at the ends the next and prev are considered as 0. 
               int next = (i == flowerbed.length - 1) ? 0 : flowerbed[i + 1]; 
               int prev = (i == 0) ? 0 : flowerbed[i - 1];
               if(next == 0 && prev == 0) {
                   flowerbed[i] = 1;
                   count++;
               }
            }
	    }

	    return count>=n;
    }
}