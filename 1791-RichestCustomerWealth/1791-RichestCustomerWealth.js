// Last updated: 6/25/2025, 11:42:49 AM
/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let richest = 0
    for (i = 0; i < accounts.length; i++){
        let current = 0
        for (j=0; j< accounts[i].length; j++){
            current += accounts[i][j]
            if(current > richest) richest = current
        }
    }
    return richest
};