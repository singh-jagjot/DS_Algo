class Solution {
    public void moveZeroes(int[] nums) {
        int swapIdx = 0;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] != 0){
                if(swapIdx != i){
                    nums[swapIdx] = nums[i];
                    nums[i] = 0;
                }
                swapIdx++;
            }
        }
    }
}