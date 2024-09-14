class Solution {
    public int rob(int[] nums) {
        int pre = 0;
        int res = nums[0];
        for(int i=1;i<nums.length;i++){
            int temp = res;
            res = Math.max(res, nums[i]+pre);
            pre = temp;
        }
        return res;
    }
}
