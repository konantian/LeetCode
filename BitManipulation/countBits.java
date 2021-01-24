public int[] countBits(int num) {
    if (num == 0)
        return new int []{0};
    if (num == 1)
        return new int [] {0, 1};
    int [] result = new int [num+1];
    result[0] = 0;
    result[1] = 1;
    for (int i=2; i<=num; i++) {
        if (i % 2 == 0) {
             result[i] = result[i/2];
        }
        else
            result[i] = 1 + result[i/2];
    }
    return result;
}