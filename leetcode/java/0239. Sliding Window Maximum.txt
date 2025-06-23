class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] res = new int[nums.length + 1 - k];
        Deque<Integer> dq = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++) {
            //Remove indices that are now outside the window (from left)
            if (!dq.isEmpty() && dq.peekFirst() + k <= i) //Can use 'dq.peekFirst() + k == i' as well
                dq.pollFirst();

            //Removing smaller/equal redundant values
            while (!dq.isEmpty() && nums[i] >= nums[dq.peekLast()])
                dq.pollLast();

            dq.offerLast(i);

            if (i + 1 >= k)
                res[i + 1 - k] = nums[dq.peekFirst()];
        }

        return res;
    }
}