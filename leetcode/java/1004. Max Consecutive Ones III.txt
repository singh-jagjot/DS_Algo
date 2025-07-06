//Variable Sliding Window

class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int zeros = 0;
        int max = 0;

        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                zeros++;
            }

            while (zeros > k) {
                if (nums[left] == 0) {
                    zeros--;
                }
                left++;
            }
            max = Math.max(max, right - left + 1);
        }
        return max;
    }
}

// OR

//Not that efficient but works, my initial submission
//class Solution {
//
//   public int longestOnes(int[] nums, int k) {
//        int flipped = 0;
//        int left = 0, right = 0;
//        int max = 0;
//        int currMax = 0;
//        while (left < nums.length && right < nums.length) {
//            if (flipped < 0)
//                flipped = 0;
//
//            if (left > right) {
//                right++;
//            }
//
//            int valLeft = nums[left];
//            int valRight = nums[right];
//            if (valRight == 0) {
//                if (flipped < k) {
//                    flipped++;
//                    right++;
//                } else {
//                    if (valLeft == 0) {
//                        flipped--;
//                    }
//                    left++;
//                }
//            } else {
//                right++;
//            }
//            currMax = right - left;
//            max = Math.max(max, currMax);
//        }
//        return max;
//    }
//}