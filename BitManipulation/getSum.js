var getSum = function(a, b) {
    while(b != 0){
        const c = a & b;
        a = a ^ b;
        b = c << 1;
    }
    return a;
};