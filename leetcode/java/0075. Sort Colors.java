class Solution {
    public void sortColors(int[] nums) {
        int left = 0;               // Boundary for 0s
        int right = nums.length - 1; // Boundary for 2s
        int current = 0;             // Pointer to scan the array

        while (current <= right) {
            if (nums[current] == 0) {
                swap(nums, left, current);
                left++;
                current++;
            } else if (nums[current] == 2) {
                swap(nums, current, right);
                right--;
                // Don't increment current here to re-evaluate the swapped value
            } else {
                current++;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
