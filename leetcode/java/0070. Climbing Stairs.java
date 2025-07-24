// Time: O(n), Space: O(1)
class Solution {
    public int climbStairs(int n) {
        if(n<3) return n;
        int pre=1,curr=2;
        int temp=0;
        for(int i=3;i<=n;i++){
            temp = curr;
            curr = pre+curr;
            pre = temp;
        }
        return curr;
    }
}