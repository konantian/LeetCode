/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */

var selfDividingNumbers = function(left, right) {
    let result = [];
    for(let i = left;i<= right;i++){
        if(canDivideByItself(i)) result.push(i);
    }
    return result;
};

var canDivideByItself = function(n){
    let t = n;
    while(t > 0){
        digit = t % 10;
        if(digit == 0 || n % digit != 0) return false;
        t = Math.floor(t/10);
    }
    return true;
}