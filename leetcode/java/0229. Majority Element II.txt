class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int me1=0,me2=0,c1=0,c2=0;

        for(int num:nums){
            if(num==me1) c1++;
            else if(num==me2) c2++;
            else if(c1==0){
                me1=num;
                c1++;
            } else if(c2==0){
                me2=num;
                c2++;
            } else {
                c1--;
                c2--;
            }
        }
        c1=0;c2=0;
        for(int num:nums){
            if(me1==num) c1++;
            else if(me2==num) c2++;
        }
        List<Integer> res = new ArrayList<>();
        if(c1>nums.length/3) res.add(me1);
        if(c2>nums.length/3) res.add(me2);
        return res;
    }
}