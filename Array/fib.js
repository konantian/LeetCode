/**
 * @param {number} N
 * @return {number}
 */
var fib = function(N) {
    let a = 0;
    let b = 1;
    let temp = 0;
    for(let i = 0;i<N;i++){
        temp = a;
        a = b;
        b += temp;
    }
    return a;
};