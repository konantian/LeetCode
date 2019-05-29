/**
 * @param {number[]} A
 * @return {number}
 */
var repeatedNTimes = function(A) {
    let counter = [];
    for(let i of A){
        if(counter.includes(i)) return i;
        counter.push(i);
    }
};