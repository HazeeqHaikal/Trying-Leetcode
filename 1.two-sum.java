/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start

import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[] res = new int[2];
        int len = nums.length;
        for (int i = 0; i < len; i++) {
            int num = nums[i];
            int diff = target - num;
            for (int j = i + 1; j < len; j++) {
                if (nums[j] == diff) {
                    res[0] = i;
                    res[1] = j;
                    return res;
                }
            }
        }

        return res;

    }
}
// @lc code=end
