public boolean isPowerOfFour(int n) {
	if(n <= 0) return false;
	if((n & (n-1)) != 0) return false;
	int total = 0;
	while(n > 1){
		total++;
		n = n >> 1;
	}
	return (total & 1) == 0;
}