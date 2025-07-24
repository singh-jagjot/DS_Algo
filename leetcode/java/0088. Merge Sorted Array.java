class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int idx = m + n - 1; // Index to place the next largest element
        int i = m - 1; // Pointer for nums1
        int j = n - 1; // Pointer for nums2

        // Merge in reverse order
        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[idx--] = nums1[i--];
            } else {
                nums1[idx--] = nums2[j--];
            }
        }
    }
}