//Kadane's Algorithm
//Time: O(n), Space:O(1)
class Solution {
   public int maxSubArray(int[] nums) {
        int sum = 0;
        int maxSoFar = nums[0];
        for(int num:nums){
            sum = Math.max(num, sum+num);
            if(sum>maxSoFar) maxSoFar=sum;
        }
        return maxSoFar;
    }
}
