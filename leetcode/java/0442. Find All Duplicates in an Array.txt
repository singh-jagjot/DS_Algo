class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> lst = new ArrayList<>();
        for(int i = 0; i<nums.length; i++){
            int curr = Math.abs(nums[i]);
            int idx = curr - 1;
            if(nums[idx] < 0){
                lst.add(Math.abs(curr));
            } else {
                nums[idx] *= -1;
            }
        }
        return lst;
    }
}