class Solution {
    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // We compare the middle element with its right neighbor
            if (nums[mid] < nums[mid + 1]) {
                // We are on an upward slope.
                // The peak must be to the right (and could be mid + 1).
                left = mid + 1;
            } else {
                // We are on a downward slope.
                // The peak is either 'mid' or to its left.
                right = mid;
            }
        }

        // When left == right, we've converged on a peak element.
        return left;
    }
}

//My Solution(Above is recommended)
class Solution {
    public int findPeakElement(int[] nums) {
        if(nums.length == 1) return 0;
        if(nums[0]>nums[1]) return 0;
        if(nums[nums.length-1]>nums[nums.length-2]) return nums.length-1;
        int left = 1;
        int right = nums.length - 2;
        while(left<=right){
            int mid = left+(right-left)/2;
            if(nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1]) return mid;
            else if(nums[mid] < nums[mid-1]) right = mid-1;
            else left = mid+1;
        }
        return -1;
    }
}