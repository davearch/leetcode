/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const numSet = new Set();
    for (var i = 0; i < nums.length; i++) {
        let num = nums[i];
        if (numSet.has(num)) {
            return true;
        }
        numSet.add(num)
    }
    return false;
};