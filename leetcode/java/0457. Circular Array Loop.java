class Solution {
    public boolean circularArrayLoop(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            // already visited or 0 can't move
            if (nums[i] == 0) continue;

            boolean isForward = nums[i] > 0;
            int slow = i, fast = i;

            while (true) {
                slow = getNextIdx(nums, isForward, slow);
                fast = getNextIdx(nums, isForward, fast);
                if (fast != -1) fast = getNextIdx(nums, isForward, fast);
                if (slow == -1 || fast == -1) break;
                if (slow == fast) return true;
            }

            // Mark all visited nodes in this path as 0 (invalid)
            int curr = i;
            while (true) {
                int next = getNextIdx(nums, isForward, curr);
                nums[curr] = 0;
                if (next == -1) break;
                curr = next;
            }
        }
        return false;
    }

    private int getNextIdx(int[] nums, boolean isForward, int currIdx) {
        boolean direction = nums[currIdx] >= 0;
        if (direction != isForward) return -1;

        int n = nums.length;
        int nextIdx = ((currIdx + nums[currIdx]) % n + n) % n;
        if (nextIdx == currIdx) return -1; // self-loop
        return nextIdx;
    }
}
