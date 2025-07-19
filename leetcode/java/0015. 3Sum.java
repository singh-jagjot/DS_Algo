import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // skip duplicates
            if (nums[i] > 0) break; // optimization: can't sum to 0 if nums[i] > 0

            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return res;
    }
}

//class Solution {
//    public List<List<Integer>> threeSum(int[] nums) {
//        Arrays.sort(nums);
//        List<List<Integer>> res = new ArrayList<>();
//        int curr = 0;
//        while (curr < nums.length - 2) {
//            if (curr > 0 && nums[curr] == nums[curr - 1]) {
//                curr++;
//                continue;
//            }
//            int left = curr + 1;
//            int right = nums.length - 1;
//            while (left < right) {
//                int currSum = nums[curr] + nums[left] + nums[right];
//                if (currSum == 0) {
//                    List<Integer> temp = new ArrayList<>();
//                    temp.add(nums[curr]);
//                    temp.add(nums[left]);
//                    temp.add(nums[right]);
//                    while (left < right && nums[left] == nums[left + 1]) {
//                        left++;
//                    }
//                    while (left < right && nums[right] == nums[right - 1]) {
//                        right--;
//                    }
//                    left++;
//                    right--;
//                    res.add(temp);
//                } else if (currSum < 0) {
//                    left++;
//                } else {
//                    right--;
//                }
//            }
//            curr++;
//        }
//
//        return res;
//    }
//}