class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> prefixSumCount = new HashMap<>();
        int sum = 0;
        int count = 0;
        prefixSumCount.put(0, 1); // add 0 to handle cases where sum of subarray is equal to k

        for (int i=0;i<nums.length;i++){
            sum+=nums[i];
            if(prefixSumCount.containsKey(sum-k)) {
                count += prefixSumCount.get(sum-k);
            }
            prefixSumCount.put(sum, prefixSumCount.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
}