/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    nums.sort((a,b) => {
        if (a < b) {
            return -1;
        }
        if (a > b) {
            return 1;
        }
        return 0;
    })
    for (var i = 0; i < nums.length -1; i++) {
        if (nums[i] == nums[i + 1]) {
            return true
        }
    }
    return false;
};