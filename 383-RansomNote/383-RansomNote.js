// Last updated: 6/25/2025, 11:43:16 AM
/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    let first = {}
      for(let char of magazine){
        first[char] = (first[char] || 0) + 1
      }

    for(let char of ransomNote){
        if ( first[char] && first[char] > 0) {
            first[char] --
        } else return false
    }
    return true

};