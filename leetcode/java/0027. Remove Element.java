class Solution {
    public int removeElement(int[] nums, int val) {
        int replaceIdx = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i]!=val) {
                int temp = nums[replaceIdx];
                nums[replaceIdx] = nums[i];
                nums[i] = temp;
                replaceIdx++;
            }
        }
        return replaceIdx;
    }
}