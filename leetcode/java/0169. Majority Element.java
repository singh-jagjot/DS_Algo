//Boyer-Moore Majority Vote Algorithm
class Solution {
    public int majorityElement(int[] nums) {
        int currMe = nums[0];
        int counter = 1;
        for(int i=1;i<nums.length;i++){
            if(counter == 0){
                currMe = nums[i];
                counter++;
            } else if(nums[i]==currMe) counter++;
            else counter--;
        }
        return currMe;
    }
}