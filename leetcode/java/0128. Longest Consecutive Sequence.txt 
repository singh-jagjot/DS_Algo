class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int maxLength = 0;

        for (int num : numSet) {
            // Only try to build sequences from the start of a sequence.
            // if 'num-1' is in set then num is not a start.
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int length = 1;

                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    length++;
                }

                maxLength = Math.max(maxLength, length);
            }
        }

        return maxLength;
    }
}
