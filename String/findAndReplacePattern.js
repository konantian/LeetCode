const genPattern = (str) => {
    const map = new Map();
    let counter = 0;
    let ret = "";
    for (let i = 0; i < str.length; i++) {
        if (!map.has(str[i])) {
            map.set(str[i], counter.toString());
            counter += 1;
        }
        
        ret += map.get(str[i]);
    }
    
    return ret;
}

/**
 * @param {string[]} words
 * @param {string} pattern
 * @return {string[]}
 */
const findAndReplacePattern = function(words, pattern) {
    const p = genPattern(pattern);
    
    const result = [];
    
    for (let i = 0; i < words.length; i++) {
        if (genPattern(words[i]) === p) {
            result.push(words[i]);
        }
    }
    
    return result;
};