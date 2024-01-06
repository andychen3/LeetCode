/**
 * @param {string} s
 * @return {character}
 */
var repeatedCharacter = function(s) {
    let hashSet = new Set()
    
    for (const char of s) {
        if (hashSet.has(char)) {
            return char
        } 
        hashSet.add(char)
        
    }
    
};