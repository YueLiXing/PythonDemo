/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var runningSum = function(nums) {
    let tempRet = 0
    return nums.map((value) => {
        return tempRet += value
    })
};
console.log(runningSum([1,2,3,4]))
// console.log(runningSum([3,1,2,10,1]));